import os
try:
    from Linkedin import main_aut_linkedin
except ModuleNotFoundError as mnfe:
    if mnfe.name == 'dotenv':
        os.system('pip install python-dotenv')

    if mnfe.name == 'PIL':
        os.system('pip install pillow fonttools')

    else:
        os.system(f'pip install {mnfe.name}')
    os.system(f'python "{__file__}"')
    quit()

main_aut_linkedin.run()
