from django.shortcuts import render

# Create your views here.
def listar_tarefas(request):
	nova_tarefa = 'Assistir a Semana Python e Django da TreinaWeb'
	return render(request, 'tarefas/listar_tarefas.html', {'nova_tarefa': nova_tarefa})