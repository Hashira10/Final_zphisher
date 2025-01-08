import subprocess
from django.http import JsonResponse
from django.shortcuts import render


def show_zphisher_page(request):
    return render(request, 'zphisher.html')


# def run_zphisher(request):
#     if request.method == 'POST':
#         try:
#             # Запуск команды с помощью subprocess
#             # command = 'docker exec -it vigorous_moser bash -c "echo -e \\"1\\n1\\n2\\" | /zphisher/zphisher.sh --create-fake-login"'
#             command = 'docker exec -it tender_heisenberg bash -c "echo -e \\"1\\n1\\n2\\" | /zphisher/zphisher.sh --create-fake-login"'

#             result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
#             return JsonResponse({"output": result})
#         except subprocess.CalledProcessError as e:
#             return JsonResponse({"error": e.output}, status=500)
#     else:
#         print("Invalid request method")  # Для отладки
#         return JsonResponse({"error": "Invalid request method"}, status=400)




def run_zphisher(request):
    if request.method == 'POST':
        try:
            command = 'docker exec -it tender_heisenberg bash -c "echo -e \\"1\\n1\\n2\\" | /zphisher/zphisher.sh --create-fake-login"'
            process = subprocess.Popen(
                command, 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )

            output_lines = []
            for line in process.stdout:
                output_lines.append(line)
                # Можно передать данные по WebSocket или другим способом

            return JsonResponse({"output": "\n".join(output_lines)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)



# import subprocess
# from django.http import JsonResponse
# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')

# # def generate_fake_page(request):
# #     try:
# #         # Команда для запуска Zphisher в контейнере
# #         command = (
# #             "docker exec -it vigorous_moser bash -c "
# #             "\"echo -e '1\\n1\\n2' | /zphisher/zphisher.sh --create-fake-login\""
# #         )

# #         # Запуск команды через subprocess
# #         process = subprocess.Popen(
# #             command,
# #             stdout=subprocess.PIPE,
# #             stderr=subprocess.PIPE,
# #             shell=True,
# #             universal_newlines=True
# #         )
# #         stdout, stderr = process.communicate()

# #         if process.returncode == 0:
# #             # Извлечение ссылки из вывода команды
# #             fake_url = extract_fake_url(stdout)
# #             if fake_url:
# #                 return JsonResponse({'status': 'success', 'fake_url': fake_url})
# #             else:
# #                 return JsonResponse({'status': 'error', 'message': 'URL не найден в выводе.'})
# #         else:
# #             return JsonResponse({'status': 'error', 'message': stderr})

# #     except Exception as e:
# #         return JsonResponse({'status': 'error', 'message': str(e)})


# def generate_fake_page(request):
#     try:
#         # Команда для запуска Zphisher в контейнере
#         command = (
#             "docker exec -it vigorous_moser bash -c "
#             "\"echo -e '1\\n1\\n2' | /zphisher/zphisher.sh --create-fake-login\""
#         )

#         # Запуск команды через subprocess
#         process = subprocess.Popen(
#             command,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             shell=True,
#             universal_newlines=True
#         )
#         stdout, stderr = process.communicate()

#         if process.returncode == 0:
#             # Возвращаем весь вывод команды вместо ссылки
#             return JsonResponse({'status': 'success', 'output': stdout.strip()})
#         else:
#             return JsonResponse({'status': 'error', 'message': stderr.strip()})

#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


# def extract_fake_url(output):
#     """
#     Функция для извлечения URL из вывода Zphisher.
#     Предполагается, что URL начинается с http или https.
#     """
#     for line in output.splitlines():
#         if line.startswith("http"):
#             return line.strip()
#     return None
