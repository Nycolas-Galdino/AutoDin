from .get_credentials import get_credentials
from .exceptions import PostAlreadyPublishedError
from .create_linkedin_post import (create_linkedin_post,
                                   create_linkedin_post_with_image)


def create_post():
    (API_KEY,
     API_SECRET,
     USER_ID,
     ACCESS_TOKEN,
     EXPIRES_IN) = get_credentials()

    # text = input("Enter the text: ")
    text = open("AutodIn_Project/Linkedin/test_text.txt", "r",
                encoding="utf-8").read()

    choise = input("Do you want to post an image? (y/n): ")
    if choise == 'y':
        image_path = input("Enter the path to the image: ")
        create_linkedin_post_with_image(bearer_token=ACCESS_TOKEN,
                                        user_id=USER_ID,
                                        text=text,
                                        image_filepath=image_path,
                                        visibility="PUBLIC")
    else:
        create_linkedin_post(bearer_token=ACCESS_TOKEN,
                             user_id=USER_ID,
                             text=text,
                             visibility="PUBLIC")

    print('POST REALIZADO COM SUCESSO!')


def run():
    try:
        create_post()
    except Exception as e:
        print(e, e.errno)
        if e.errno == 422:
            raise PostAlreadyPublishedError from e
