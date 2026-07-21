from talon import Module, actions

mod = Module()

# Track OpenWhispr's state independently
open_whispr_active = False

@mod.action_class
class Actions:
    def toggle_open_whispr_safely():
        """Toggles OpenWhispr and always forces Talon awake when finished"""
        global open_whispr_active

        if not open_whispr_active:
            # --- WE ARE STARTING OPENWHISPR ---
            open_whispr_active = True

            # Only disable Talon if it's actually awake to prevent the pop-up
            if actions.speech.enabled():
                actions.speech.disable()

            # Trigger OpenWhispr to start listening
            actions.key("ctrl-shift-f9")

        else:
            # --- WE ARE STOPPING OPENWHISPR ---
            open_whispr_active = False

            # Trigger OpenWhispr to stop listening
            actions.key("ctrl-shift-f9")

            # Wake Talon back up
            if not actions.speech.enabled():
                actions.speech.enable()

            # Force Talon into command mode
            actions.mode.enable("command")
            actions.mode.disable("sleep")
            actions.mode.disable("dictation")
