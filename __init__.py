from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

_author__ = 'prasad'
LOGGER = getLogger(__name__)

class TicketSkill(MycroftSkill):
# 	def get_numerical_response(self, dialog):
	def  enter_source_destination(stops):
    	while True:
        	source = input('Enter your boarding bus stop: ')
        	if source in stops:
            	while True:
                	destination = input('Enter your destination: ')
                	if destination in stops:
                    	return source, destination
                	else:
                    	print('Could you please enter a valid destination stop')
                    	continue
        	else:
            	print('Could you please enter a valid boarding point')
            	continue

	stops = ['vizag', 'hyderabad', 'vijayawada']
	source, destination = enter_source_destination(stops)
self.speak('The sourceing point is ', source, 'and the destination is ', destination)
@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
def handle_start_game_intent(self, message):
	self.speak_dialog("start.game")
	self.speak('The sourceing point is ', source, 'and the destination is ', destination)
		
		
	def stop(self):
		pass
def create_skill():
	return TicketSkill()
