@namespace
class SpriteKind:
    background = SpriteKind.create()

def on_a_pressed():
    global Playing
    if Playing == 0:
        music.play(music.string_playable("D F E G F D G E ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        Playing = 1
        scene.camera_shake(2, 2000)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

Playing = 0
info.set_score(0)
Background = sprites.create(assets.image("""
    cityscape2
"""), SpriteKind.background)
game.show_long_text("Press \"A\" To start the game!", DialogLayout.BOTTOM)