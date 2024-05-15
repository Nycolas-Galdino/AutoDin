import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Objects.Obj_Requests import Request
from Objects.Obj_TextConverter import TextConverter


def create_linkedin_post(bearer_token: str,
                         user_id: str,
                         text: str,
                         visibility: str = "PUBLIC"):
    obj_convert = TextConverter()
    text = obj_convert.convert_text(text)
    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
    }

    data = {
        "author": user_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "attributes": [],
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": visibility
        }
    }

    Request.post(url, headers=headers, data=data)


def create_linkedin_post_with_image(bearer_token: str,
                                    user_id: str,
                                    text: str,
                                    image_filepath: str,
                                    visibility: str = "PUBLIC",
                                    **kwargs):
    obj_convert = TextConverter()
    text = obj_convert.convert_text(text)
    image_filepath = image_filepath.replace("\\", "/")
    image_id = _upload_image(bearer_token, user_id, image_filepath)

    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
    }

    data = {
        "author": user_id,
        "lifecycleState": kwargs.get("lifecycleState", "PUBLISHED"),
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": kwargs.get("shareMediaCategory", "IMAGE"),
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": "Imagem gerada por inteligência aritificial"
                        },
                        "media": image_id
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": visibility
        }
    }

    res = Request.post(url, headers=headers, data=data)
    print('Post:', res)


def _create_image_id(bearer_token: str, user_id: str) -> tuple:
    url = 'https://api.linkedin.com/v2/assets?action=registerUpload'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
    }

    body: dict = {
        "registerUploadRequest": {
            "recipes": [
                "urn:li:digitalmediaRecipe:feedshare-image"
            ],
            "owner": user_id,
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ]
        }
    }

    r = Request.post(url, headers=headers, data=body)['value']
    upload_url = r['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    asset = r['asset']

    return upload_url, asset


def _upload_image(bearer_token: str, user_id: str, image_filepath: str) -> str:
    upload_url, asset = _create_image_id(bearer_token, user_id)

    headers = {"Authorization": f"Bearer {bearer_token}"}
    Request.post(upload_url, headers=headers, data=open(image_filepath, 'rb'))
    return asset
