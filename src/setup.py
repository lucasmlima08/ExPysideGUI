from cx_Freeze import setup, Executable

setup(
    name = "Soma",
    version = "0.1",
    description = "Soma de Numeros",
    executables = [Executable("SomaDeDoisNumeros.py",base="Win32GUI")]
)

# python setup.exe build
