import bpy

translations = {
    "pt_BR": {
        ("*", "Convert to Plain Axes"): "Converter para Eixos Simples",
        ("*", "Create HDR Matcap"): "Criar Matcap HDR",
    },
    "en_US": {
        ("*", "Convert to Plain Axes"): "Convert to Plain Axes",
        ("*", "Create HDR Matcap"): "Create HDR Matcap",
    }
}

def register_translation():
    for lang, data in translations.items():
        bpy.app.translations.register(__name__ + "_" + lang, data)

def unregister_translation():
    for lang in translations.keys():
        bpy.app.translations.unregister(__name__ + "_" + lang)
