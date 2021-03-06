import "./lib/handlebar.js"

function show_password(form_id:string) {
    // function for revealing password data from password field
    var form_instance:any = document.getElementById(form_id);

    if (form_instance.type === "password") {
        // change the form type to text to reveal the password data
        form_instance.type = "text";
    } else {
        form_instance.type = "password";
    }
}

function caps_lock_on(field_id:string, message_div_id:string){
    // display cas lock is on message
    const message:string = "Caps lock is On."
    // Get field instance
    var input:any = document.getElementById(field_id)

    input.addEventListener("keyup", (event:any) => {
        if (event.getModifiedState("CapsLock")){
            // display message
            document.getElementById(message_div_id).innerHTML = message
        } else {
            // Hide message
            document.getElementById(message_div_id).innerHTML = ""
        }
    })
}

function copy_to_clipboard(input_id:string){
    var input_instance:any = document.getElementById(input_id)

    input_instance.select()
    input_instance.setSelectionRange(0, 99999) // for mobile devices

    document.execCommand("copy")
    input_instance.clearSelected()
    // Note: The document.execCommand() method is not supported in IE8 and earlier.
}

function disable_btn(btn_id:string) {
    document.getElementById(btn_id).disabled = true;
}

export { copy_to_clipboard, caps_lock_on, show_password, disable_btn }