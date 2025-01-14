[[!meta title="Mail virtual hosting for student groups"]]


Our regular virtual hosting gives your group a website at
`mygroup.studentorg.berkeley.edu`. By contrast, *mail virtual hosting* lets you create as
many email addresses as you'd like `@mygroup.studentorg.berkeley.edu`.

These addresses can be used both to receive mail (via mail forwarding), and
send mail. The details of how to use these addresses are below.


## Getting set up with mail virtual hosting

By default, groups only have regular web virtual hosting.

If you'd like to get started using mail virtual hosting, you should set up
a group account and
[request a vhost from us](https://www.ocf.berkeley.edu/docs/services/vhost/#h3_instructions),
if you have not already. Please include that you would like mail virtual hosting
in your request for a vhost. If you already have a vhost with us, send
us an email at [hostmaster@ocf.berkeley.edu](mailto:hostmaster@ocf.berkeley.edu)
letting us know you'd like to enable email virtual hosting. Be sure to include both the
domain name, and your OCF account name.

Once your domain is configured for mail, head over to our [[mail
virtual hosting page|vhost_mail]] to add and remove addresses.


## How sending and receiving mail works

The OCF does not provide "true" mail hosting -- we do not store mail on our
servers, nor do we provide a new mailbox for you to monitor. Instead, we
provide:

* Mail forwarding: forward emails sent to `xxxx@yourgroup.studentorg.berkeley.edu` to an
  email address you already own.
* Mail sending: send an email as `xxxx@yourgroup.studentorg.berkeley.edu`.
* Lightweight user management: create different email addresses and configure
  who to forward them to.

Our admin panel looks like this:
![](https://i.fluffy.cc/9cGLcQv29G6kmlgvnvgq8J7nxw9BlMrx.png)

We provide instructions for setting this up with Gmail below, but other email
providers and clients offer similar options.

#### How can I use Gmail to send and receive email?

[[We have an entire page about that — click here!|doc
services/vhost/mail/gmail]]


#### How can I use an email client besides Gmail to send and receive email?

There are too many email clients for us to provide instructions for, so here
are the settings you'll need:

* **SMTP server:** `smtp.ocf.berkeley.edu`
* **Port:** 587
* **Security:** TLS, verify cert
* **Username:** The full email address, including domain name
* **Password:** The password you set

Note that we *only provide email sending*, so you only need to configure SMTP
and not POP/IMAP.

Good luck!



#### What if I only want to receive and not send email?

You can totally do that! Just set up an address to forward to and don't bother
configuring the sending address. You can even leave the password blank.
