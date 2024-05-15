import re

class TextConverter:
    def __init__(self):
        self.ascii_to_math_bold = {
            'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
            'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
            'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
            'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
            'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠',
            'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧',
            'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮',
            'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳'
        }

        self.ascii_to_small_caps = {
            'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ',
            'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ',
            'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ',
            'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ'
        }

    def convert_to_style(self, text, style_mapping):
        return ''.join(style_mapping.get(c, c) for c in text)

    def replace_styled_text(self, match):
        full_match = match.group(0)
        if full_match.startswith('**'):
            content = match.group(1)
            return self.convert_to_style(content, self.ascii_to_math_bold)
        elif full_match.startswith('__'):
            content = match.group(2)
            return self.convert_to_style(content.upper(), self.ascii_to_small_caps).lower()
        return full_match

    def convert_text(self, texto):
        # Expressão regular para encontrar partes entre ** e __
        pattern = re.compile(r'\*\*(.*?)\*\*|__(.*?)__')

        # Substitui partes formatadas usando a função replace_styled_text
        converted_text = pattern.sub(self.replace_styled_text, texto)

        return converted_text

def main():
    texto = """
    
    *ISSO É UM TESTE EM POST COM API*
    **Explorando Dados Rapidamente com Pandas-Profiling 📊**
    
    __O que é pandas?__
    
    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nostrum impedit, dolores sit odio ipsa et! Laborum quam neque impedit cumque commodi maxime possimus, quas ipsam tempore, iusto consequatur fugit non!    
    
    __como utilizar PANDAS?__
    
    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nostrum impedit, dolores sit odio ipsa et! Laborum quam neque impedit cumque commodi maxime possimus, quas ipsam tempore, iusto consequatur fugit non!
    
    By **nycolas Pimentel**
    """

    converter = TextConverter()
    converted_text = converter.convert_text(texto)
    print(converted_text)

if __name__ == "__main__":
    main()
