from talon import Module, actions, app

mod = Module()

# Fallback mic if active_microphone() isn't ready on boot
last_mic = "System Default"

@mod.action_class
class Actions:
    def talon_mute():
        """Disconnect Talon from the microphone completely"""
        global last_mic
        current = actions.sound.active_microphone()
        if current and current.lower() != "none":
            last_mic = current
        actions.sound.set_microphone("None")

        # Also put Talon to sleep such that the icon changes.
        if actions.speech.enabled():
            actions.speech.disable()

    def talon_unmute():
        """Reconnect Talon to the last active microphone"""
        global last_mic
        actions.sound.set_microphone(last_mic)

        # Also wake up Talon such that the icon changes.
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
    """Capture initial active mic and mute Talon on startup"""
    actions.user.talon_mute()

app.register("ready", on_ready)
