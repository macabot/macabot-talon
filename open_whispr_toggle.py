from talon import Module, actions

mod = Module()

# Tracks the physical key to prevent OS key-repeat spam
open_whispr_is_holding = False


@mod.action_class
class Actions:
    def open_whispr_start():
        """Triggered when F10 is initially pressed down"""
        global open_whispr_is_holding

        # If the OS sends a repeated "key down" while we are already holding it, ignore it!
        if open_whispr_is_holding:
            return

        open_whispr_is_holding = True
        actions.user.talon_mute()
        actions.key("ctrl-shift-f9")

    def open_whispr_stop():
        """Triggered when F10 is released"""
        global open_whispr_is_holding

        open_whispr_is_holding = False
        actions.key("ctrl-shift-f9")
        actions.user.talon_unmute()
