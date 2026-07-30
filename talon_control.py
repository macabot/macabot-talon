from talon import Module, actions, app

mod = Module()

# Using "System Default" ensures Talon always follows your Ubuntu Sound Settings
TARGET_MIC = "System Default"

@mod.action_class
class Actions:
    def talon_mute():
        """Disconnect Talon from the microphone completely"""
        actions.sound.set_microphone("None")

        # Put Talon to sleep so the tray icon updates visually
        if actions.speech.enabled():
            actions.speech.disable()

    def talon_unmute():
        """Reconnect Talon to the System Default microphone"""
        actions.sound.set_microphone(TARGET_MIC)

        # Wake Talon up so the tray icon updates visually
        if not actions.speech.enabled():
            actions.speech.enable()

    def talon_toggle_mute():
        """Toggle Talon microphone on/off"""
        current = actions.sound.active_microphone()
        if not current or current.lower() == "none":
            actions.user.talon_unmute()
        else:
            actions.user.talon_mute()

def on_ready():
    """Mute Talon on startup"""
    actions.user.talon_mute()

app.register("ready", on_ready)
