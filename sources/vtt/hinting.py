from fontTools.ttLib import TTFont
import vttLib
from gftools.scripts.transfer_vtt_hints import transfer_hints


sources = {
    "sources/vtt/Gontserrat[wght]-VTT.ttf": "fonts/variable/Gontserrat[wght].ttf",
    "sources/vtt/Gontserrat-Italic[wght]-VTT.ttf": "fonts/variable/Gontserrat-Italic[wght].ttf", 
}

print("INFO:Integrating hinting sources and compiling")

for src, dst in sources.items():
    src = TTFont(src)
    dst = TTFont(dst)
    transfer_hints(src, dst)
    vttLib.compile_instructions(dst, ship=True)
    dst["head"].flags |= 1 << 3
    dst.save(dst.reader.file.name)
