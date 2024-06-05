from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AudioMenschen, AudioGrammatik_Aktiv
from django.http import FileResponse
from zipfile import ZipFile
from io import BytesIO
import os

# @login_required(login_url='/login/')
# def menschen_audio(request):
#     class_level = request.GET.get('class_level', None)
#     audio_resources = AudioMenschen.objects.filter(audio__class_level=class_level).distinct() if class_level else None

#     if audio_resources:
#         audio_files = []
#         for audio_resource in audio_resources:
#             zip_file = audio_resource.zip_file
#             if zip_file:
#                 zip_contents = BytesIO(zip_file.read())
#                 with ZipFile(zip_contents, 'r') as zip_ref:
#                     for file_name in zip_ref.namelist():
#                         if file_name.endswith('.mp3') or file_name.endswith('.wav'):
#                             file_path = file_name
#                             audio_files.append((file_name, file_path))

#         context = {
#             'audio_resources': audio_resources,
#             'audio_files': audio_files,
#         }
#     else:
#         context = {
#             'audio_resources': None,
#             'audio_files': [],
#         }

#     return render(request, 'audio_menschen.html', context)
def menschen_audio(request):
    class_level = request.GET.get('class_level', None)
    audio_resources = AudioMenschen.objects.filter(audio__class_level=class_level).distinct() if class_level else None

    if audio_resources:
        audio_files = []
        for audio_resource in audio_resources:
            zip_file = audio_resource.zip_file
            if zip_file:
                zip_contents = BytesIO(zip_file.read())
                with ZipFile(zip_contents, 'r') as zip_ref:
                    for file_name in zip_ref.namelist():
                        if file_name.endswith('.mp3') or file_name.endswith('.wav'):
                            file_path = file_name  # or generate the path if needed
                            audio_id = audio_resource.id  # assuming audio_resource has an id field
                            audio_files.append((file_name, file_path, audio_id))

        context = {
            'audio_resources': audio_resources,
            'audio_files': audio_files,
        }
    else:
        context = {
            'audio_resources': None,
            'audio_files': [],
        }

    return render(request, 'audio_menschen.html', context)

#@login_required(login_url='/login/')
# def grammar_audios(request):
#     class_level = request.GET.get('class_level', None)
#     audio_grammar = AudioGrammatik_Aktiv.objects.filter(
#         audio__class_level=class_level).distinct() if class_level else None

#     if audio_grammar:
#         audio_files = []
#         print("accessed this location")
#         for audio_resource in audio_grammar:
#             zip_file = audio_resource.zip_file
#             if zip_file:
#                 zip_contents = BytesIO(zip_file.read())
#                 with ZipFile(zip_contents, 'r') as zip_ref:
#                     for file_name in zip_ref.namelist():
#                         if file_name.endswith('.mp3') or file_name.endswith('.wav'):
#                             file_path = file_name
#                             audio_files.append((file_name, file_path))

#         context = {
#             'audio_grammar': audio_grammar,
#             'audio_files': audio_files,
#         }
       
#     else:
#         context = {
#             'audio_grammar': None,
#             'audio_files': [],
#         }
#     print(context)   

#     return render(request, 'audio_grammar.html', context)


# @login_required(login_url='/login/')

def grammar_audios(request):
    # Log the full request to see what is being passed
    print(f"Request GET parameters: {request.GET}")

    # Retrieve the class_level parameter from the GET request
    class_level = request.GET.get('class_level', None)
    print(f"class_level: {class_level}")

    # Fetch the AudioGrammatik_Aktiv objects based on the class_level
    if class_level:
        audio_grammar = AudioGrammatik_Aktiv.objects.filter(
            audio__class_level=class_level
        ).distinct()
        print(f"audio_grammar: {audio_grammar}")
    else:
        audio_grammar = None
        print("No class_level provided")

    # Process the audio files if any audio_grammar records are found
    if audio_grammar:
        audio_files = []
        print("Accessed this location")
        for audio_resource in audio_grammar:
            zip_file = audio_resource.zip_file
            print(f"zip_file: {zip_file}")

            if zip_file:
                zip_contents = BytesIO(zip_file.read())
                with ZipFile(zip_contents, 'r') as zip_ref:
                    for file_name in zip_ref.namelist():
                        print(f"Found file in zip: {file_name}")

                        if file_name.endswith('.mp3') or file_name.endswith('.wav'):
                            file_path = file_name
                            audio_files.append((file_name, file_path))
                            print(f"Added audio file: {file_name}")

        context = {
            'audio_grammar': audio_grammar,
            'audio_files': audio_files,
        }
    else:
        context = {
            'audio_grammar': None,
            'audio_files': [],
        }
    print(context)
    return render(request, 'audio_grammar.html', context)
    


def audios_view(request):
    return render(request, 'audio_landing.html', {})















def download_audio(request, audio_id, file_path):
    audio = AudioMenschen.objects.get(id=audio_id)
    zip_file = audio.zip_file
    if zip_file:
        zip_contents = BytesIO(zip_file.read())
        with ZipFile(zip_contents, 'r') as zip_ref:
            file_content = zip_ref.read(file_path)
            response = FileResponse(BytesIO(file_content), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        return None


def download_grammar_audio(request, audio_id, file_path):
    audio = AudioGrammatik_Aktiv.objects.get(id=audio_id)
    zip_file = audio.zip_file
    if zip_file:
        zip_contents = BytesIO(zip_file.read())
        with ZipFile(zip_contents, 'r') as zip_ref:
            file_content = zip_ref.read(file_path)
            response = FileResponse(BytesIO(file_content), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        return None
