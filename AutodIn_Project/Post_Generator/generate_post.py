from os.path import join, dirname
from PIL import Image, ImageDraw, ImageFont
import textwrap


def generate_post():
    text = 'Explorando Dados Rapidamente com Pandas-Profiling 📊'
    _generate_intro(text)
    _generate_details()
    _generate_end()


def _generate_intro(text):

    text = textwrap.fill(text, 30)

    # Carregando a imagem de fundo
    img = join(dirname(__file__), 'src/background_post/1.png')
    img = Image.open(img)
    bg_size = img.size

    font_file = join(dirname(__file__), 'src/fonts/Sanchez-Regular.ttf')
    font = ImageFont.truetype(font_file, 60)

    draw = ImageDraw.Draw(img)
    draw.text(
        xy=(bg_size[0] / 2, bg_size[1] / 2),
        text=text,
        font=font,
        align='center',
        fill='white',
        embedded_color='blue',
        anchor='ms')

    # Salvando a imagem final
    img.save('tela_final.png')


def _generate_details():
    pass


def _generate_end():
    pass


if __name__ == "__main__":
    generate_post()
