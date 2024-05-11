import os
try:
    from Linkedin import main_aut_linkedin
except ModuleNotFoundError as mnfe:
    os.system(f'pip install --use-pep517 {mnfe.name}')
    os.system(f'python "{__file__}"')
    quit()

main_aut_linkedin.run()
