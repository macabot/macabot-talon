from talon import Module, actions

mod = Module()

# Tracks the physical key to prevent OS key-repeat spam
open_whispr_is_holding = False


@mod.action_class
class Actions:
    def whisper_start():
        """Triggered when F10 is initially pressed down"""
        global open_whispr_is_holding

        # If the OS sends a repeated "key down" while we are already holding it, ignore it!
        if open_whispr_is_holding:
            return

        open_whispr_is_holding = True

        # Hard-disable Talon
        if actions.speech.enabled():
            actions.speech.disable()

        # Send a single TAP of the hotkey to toggle Whisper ON
        actions.key("ctrl-shift-f9")

    def whisper_stop():
        """Triggered when F10 is released"""
        global open_whispr_is_holding
        open_whispr_is_holding = False

        # Send a single TAP of the hotkey to toggle Whisper OFF
        actions.key("ctrl-shift-f9")

        # Wake Talon back up
        if not actions.speech.enabled():
            actions.speech.enable()

        # Force Talon into command mode
        actions.mode.enable("command")
        actions.mode.disable("sleep")
        actions.mode.disable("dictation")
