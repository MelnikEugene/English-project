from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Solution
from .models import Word
from .forms import TranslationForm

def about_view(request):
    return render(request, 'tasks/about.html')

def contact_view(request):
    return render(request, 'tasks/contact.html')
     
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        solution_text = request.POST.get('solution_text')
        Solution.objects.create(task=task, text=solution_text)
        return redirect('task_detail', task_id=task_id)
    return render(request, 'task_detail.html', {'task': task})

def translation_task(request):
    words = Word.objects.all()
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            score = 0
            for word in words:
                user_answer = form.cleaned_data.get(f'translation_{word.id}', '').lower().strip()
                if user_answer == word.english.lower():
                    score += 1
            return render(request, 'tasks/translation_result.html', {'score': score, 'total': words.count()})
    else:
        form = TranslationForm()
    return render(request, 'tasks/translation_task.html', {'form': form})


