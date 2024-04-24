# import subprocess
#
# libraries = ['numpy', 'matplotlib', 'customtkinter']
# for lib in libraries:
#     subprocess.call(['pip', 'install', lib])


from interface import CustomFractalApp


if __name__ == "__main__":
    app_instance = CustomFractalApp()
    app_instance.run_app()
