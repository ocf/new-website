import pexpect
from django.conf import settings

def run_approve(real_name, calnet_uid, account_name, email_address, forward_mail, password):
    try:
        child = pexpect.spawn(settings.APPROVE_BIN)

        child.expect("The authenticity", timeout=timeout_sec)
        child.sendline("yes")
        
        child.expect("Is this", timeout=timeout_sec)
        child.sendline("i")
    except:
        raise Exception("Could not run approval program.")

    try:
        child.expect("Real name", timeout=timeout_sec)
        child.sendline(real_name)
    except:
        raise Exception("Could not run approval program.")

    try:
        child.expect("University ID", timeout=timeout_sec)
        child.sendline(university_id)
    except:
        raise Exception("Error submitting name.")

    try:
        child.expect("Requested account name", timeout=timeout_sec)
        child.sendline(account_name)
    except:
        raise Exception("Error submitting ID.")

    try:
        child.expect("Enter your email address", timeout=timeout_sec)
        child.sendline(email_address)
    except:
        if "Duplicate username found in approved users file" in child.before:
            raise Exception("There is a duplicate account name awaiting approval.")
        elif "This account name has already been taken" in child.before:
            raise Exception("This account name has already been taken.")
        else:
            raise Exception("Error submitting account name.")

    try:
        child.expect("Enter again to confirm", timeout=timeout_sec)
        child.sendline(email_address)
    except:
        raise Exception("Error submitting email address.")

    try:
        child.expect("Your OCF account", timeout=timeout_sec)
        if forward_mail:
            child.sendline("y")
        else:
            child.sendline("n")
    except:
        raise Exception("Error confirming email address.")

    #shifting errors by one

    try:
        child.expect("Choose a password", timeout=timeout_sec)
        child.sendline(password)
        child.expect("Enter again to verify", timeout=timeout_sec)
        child.sendline(password)
    except:
        raise Exception("Weak password rejected.")

    try:
        child.expect("The account has been approved successfully", timeout=timeout_sec)
        print "Success"
    except:
        raise Exception("Error approving account.")
