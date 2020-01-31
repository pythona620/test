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
		home = self.get_numerical_response("get.source")
		# get upper bound
		room = self.get_numerical_response("get.destination")
# 		answer =(home + room)
# 		self.speak(answer)
	def  enter_source_destination(self,stops):
		while True:
        		source = home
        		if source in stops:
# 				self.speak(source)
            			while True:
                			destination = room
                			if destination in stops:
                    				return source, destination
                			else:
                    				self.speak_dialog(valid.source)
                    				continue
        		else:
            			self.speak_dialog(valid.destination)
            			continue

	stops = {'vizag', 'hyderabad', 'vijayawada'}
	source, destination = enter_source_destination(stops)
	self.speak('The sourceing point is ' + source + 'and the destination is' + destination)
	def stop(self):
# 		source, destination = enter_source_destination(stops)
# 		self.speak('The sourceing point is ' + source + 'and the destination is' + destination)
# 		return
		pass
def create_skill():
	return TicketSkill()
