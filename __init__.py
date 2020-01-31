from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

from random import randint

__author__ = 'prasad'
LOGGER = getLogger(__name__)

class TicketSkill(MycroftSkill):
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)	
			return val
	@intent_handler(IntentBuilder("").require("plan").optionally("going").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start")
		# get lower bound
		source = self.get_numerical_response("get.source")
		# get upper bound
		destination = self.get_numerical_response("get.destination")
		answer =(source + destination)
		self.speak(answer)
	def  enter_source_destination(stops):
    	while True:
        	source = lowerBound
        	if source in stops:
            	while True:
                	destination = upperBound
                	if destination in stops:
                    		return source, destination
                	else:
                    		self.speak('Could you please enter a valid destination stop')
                    		continue
        	else:
            		self.speak('Could you please enter a valid boarding point')
            		continue

	stops = ['vizag', 'hyderabad', 'vijayawada']
	source, destination = enter_source_destination(stops)
	self.speak('The sourceing point is ' + source + 'and the destination is' + destination)
	def stop(self):
		pass

def create_skill():
	return TicketSkill()