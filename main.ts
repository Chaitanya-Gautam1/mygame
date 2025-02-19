namespace SpriteKind {
    export const background = SpriteKind.create()
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (Playing == 0) {
        music.play(music.stringPlayable("D F E G F D G E ", 120), music.PlaybackMode.LoopingInBackground)
        Playing = 1
        scene.cameraShake(2, 2000)
    }
    
})
let Playing = 0
info.setScore(0)
let Background = sprites.create(assets.image`
    cityscape2
`, SpriteKind.background)
game.showLongText("Press \"A\" To start the game!", DialogLayout.Bottom)
