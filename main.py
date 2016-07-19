import mm2pass,random,logging

logging.basicConfig(filename=__name__.replace(".","/")+".py.log")
lumberjack = logging.getLogger(__name__)
lumberjack.info("started")
print("mm2passrand - a randomized password generator")
game = mm2pass.Game()
game.setETanks(random.randint(0,4))
for robo in game.robo_masters:
	if random.randint(1,random.randint(2,10)) == 1:
		game.defeat(robo)
print("Your password is:")
mm2pass.prettify(game.getPassword())
lumberjack.info("done")
