from django.shortcuts import render,redirect 
from django.http import HttpResponse 

# Create your views here.
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
from .training_data import list_to_train
bot=ChatBot('VVIT chatbot',read_only=False,
            logic_adapters=[
                {
                    'import_path':'chatterbot.logic.BestMatch',
                    'default_response':'Sorry,I dont know what you are asking for',
                    'maximim_similarity_threshold':0.70
                }])


list_trainer=ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request,'blog/index.html')
def specific(request):
    return HttpResponse("this is the specific url")
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
