[[!meta title="Virtual hosting (group.studentorg.berkeley.edu)"]]


Virtual hosting allows group accounts to have their website available on a
different domain, typically under berkeley.edu. For example, a group's site can
be made available at `yourgroup.studentorg.berkeley.edu` in addition to the standard
address under `ocf.berkeley.edu`. Faculty and staff are also eligible
for virtual hosting, but must obtain their own domains (e.g.
`name.dept.berkeley.edu`).

The OCF provides two separate (but related) virtual hosting services:

* **Web hosting**, where your group's OCF-hosted website becomes available
  under the new name

* **Email forwarding**, which lets you configure email forwarding for the new
  name

Web hosting is always enabled for group accounts with virtual hosting, but
email forwarding must be requested separately.

## Web Hosting

After the virtual host is set up, the files in the `public_html` directory of
your group account (ordinarily accessible at
`https://www.ocf.berkeley.edu/~accountname`) will appear at the root directory
of the virtual-hosted site (`yourgroup.studentorg.berkeley.edu`).

### Instructions

1.   **Request an account.** [[Request an OCF account|doc membership]] (if you
     haven't already done so). Student and department groups need a group
     account; faculty and staff may use their personal account.
2.   **Set up real site.** Set up your webspace and upload your website (if you
     haven't already done so). The website should be developed already, not a
     placeholder.
3.   **Include OCF hosting banner.** Place a [[Hosted by OCF banner|doc
     services/vhost/badges]] on your home page that links to the OCF front
     page. If none of these images are appropriate for your site, you may
     design one of your own and [[submit it|doc contact]] for approval.
4.   **Include university's disclaimer (if applicable).** If you are a student
     group, place the university-mandated student group disclaimer on each page
     of your website (see the section below).
5.   **Obtain a domain (faculty and staff only).** The OCF will not request
     personal domains for individuals, so faculty and staff must obtain their
     own. Your department may be able to assist you with this step.
6.   **Complete request form.** Complete the [[virtual hosting request
     form|request_vhost]] online. OCF staff will review your request and
     contact the university hostmaster on your behalf if necessary.

### Including the OCF banner {ocf_banner}

Place any of the [[Hosted by OCF banners|doc services/vhost/badges]] on your
site by copying the code onto your page. The banner need only be placed on the
home page of your site. You can also create your own OCF banner with approval
from the OCF (see instructions above).

### Including the University Student Group Disclaimer    {disclaimer}

The university [requires][rso-domains] that all student group websites on a
subdomain of berkeley.edu (other than those of university-sponsored student
groups) contain the following text on each page:

> We are a student group acting independently of the University of California.
> We take full responsibility for our organization and this web site.

## Email Forwarding    {email}

Want to send and receive email from `@mygroup.studentorg.berkeley.edu` addresses? You can
do that!

We call this *mail virtual hosting*. To learn more, [[check out our page about
that|doc services/vhost/mail]].

## Policies    {policies}

<!-- As amended by the Board of Directors on April 10, 2017. -->

### Groups, faculty, and academic staff only

The OCF only performs virtual hosting for OCF group accounts and individual
accounts belonging to UC Berkeley faculty, and the faculty and academic staff
of associated institutions which are listed in our
[[eligibility policy | doc membership/eligibility]]. Each account may have at
most one virtual host, but you are free to set up external domains which redirect
to it (see [Google Domains Help][domain-forwarding] for an example). Faculty and academic staff are not eligible for mail hosting for their
individual accounts, as mail hosting is intended for mailing lists or group
accounts. Furthermore, virtual hosts for faculty and staff will only be
approved if they have already obtained a domain name from their department or
elsewhere. Group accounts for research groups are not subject to these
restrictions. While we are happy to host personal websites for faculty and
staff, we will not manage their DNS, nor provide mailing lists for individual
accounts.

[domain-forwarding]: https://support.google.com/domains/answer/4522141#forwarddomain

### Limitations on non-berkeley.edu domains

The OCF may host non-berkeley.edu domains (e.g. 'foobarbaz.com'); however, the process is more
complicated in such cases. At the discretion of an OCF (Deputy) Site Manager,
permission may be granted to those who can demonstrate a specific need for the
OCF to host a website outside of the berkeley.edu domain. For such domains, the
account holder must:

1.  Obtain the written permission of a Site Manager or Deputy Site Manager to
    host this domain.

2.  Pay any and all fees and/or obtain permissions relating to obtaining and
    maintaining a domain name.

The OCF has considered hosting non-berkeley.edu domains when: a student group
website was previously hosted at a non-berkeley.edu address, a website
for a department or University-affiliated research group required a
particular domain, & the personal website of a faculty or staff member needed a home.
Domains under berkeley.edu may not redirect to a non-berkeley.edu domain (see
**no off-site hosting**).

### University policies

As with any OCF account, virtually hosted websites must comply with the
relevant UC Berkeley [computer use policy][computer-use] and [DNS
policy][dns-policy]. The LEAD Center's [Student Org Domain Name
Guidelines][rso-domains] presents the most relevant information to student
groups.

[computer-use]: https://security.berkeley.edu/policy/usepolicy.html
[dns-policy]: https://security.berkeley.edu/policy/dns
[rso-domains]: https://lead.berkeley.edu/wp-content/uploads/2014/12/student-org-domain-guidelines.pdf

In particular,

* **No off-site (third-party) hosting**: Circumventions around off-site
hosting, including (but not limited to) proxies, redirects, and substantial
inline frames (iframes) of non-berkeley.edu domains are not allowed. The OCF
does not process nor advise off-site hosting requests, which can be
[submitted directly to the university][offsite] (however, feel free to keep
us informed if you have an existing OCF account).

   In other words, to comply with university policy, the OCF may only provide
   virtual hosting for websites that are hosted on OCF servers.

* **Relevant domain name**: Registered Student Organizations may only use
domains or request subdomains that are the officially recognized name of the
group or a recognizable shortened version of the official name. Exceptions to
this rule must be approved by the LEAD Center prior to requesting the domain
from the OCF. In general, the subdomain must reasonably and uniquely identify
the student group that is requesting it, and not be easily confused with another
group or University department or resource.

[offsite]: https://offsitehosting.berkeley.edu/

### Hosting badge

All virtual hosts on the OCF must include an [[OCF banner|doc
services/vhost/badges]] on the front page that links to the [[OCF home
page|home]]. The banner must be noticeable without undue effort.  The hosting
badge not only attributes the OCF but also distinguishes it from sites hosted
by University departments.

### Disabling of virtual hosts

If your OCF account is found in violation of OCF policies, including but not
limited to the virtual hosting policies in this document, your account and/or
vhost may be disabled, depending on the cause of the violation. If your vhost
is disabled you will see [this](http://unavailable.ocf.berkeley.edu/) landing
page in place of your vhost.  If you would like to request a domain that points
to a currently disabled vhost, please contact us for more information.

### Reclamation of virtual hosts

Any virtual host which is no longer used, in violation of OCF policies, or
assigned to an OCF account which has lost eligibility (for instance, an account
for an inactive RSO) may be reclaimed by the OCF. This means that the domain
name will no longer be reserved for the group or individual that previously
used it, and the domain may be claimed by others. If the domain is claimed by
another group or individual after is has been reclaimed, the original group
will not be able to reclaim it unless it becomes available again.  If the
virtual host has been disabled by the explicit request of the account holder,
or if the account has lost eligibility for virtual hosting, then the virtual
host may be reclaimed immediately.  Finally, if the virtual host was disabled
for violating [[account|doc services/account/account-policies]] or vhost
policy, before reclaiming the vhost, OCF staff will make an effort to contact
the group which holds it. If, in two weeks, we receive no response or OCF staff
have determined that there has not been sufficient progress towards resolving
the issue, the virtual host will be disabled if it is not already. After a
virtual host has been disabled for 3 months, it may be reclaimed at the
discretion of the OCF staff.

### Renaming virtual hosts

If you wish to rename your virtual host (e.g. switch from
something.berkeley.edu to somethingelse.berkeley.edu), you must provide a
compelling reason for doing so, such as a change in the name of your group. In
this case, you may contact us to request a virtual host at your new URL. If the
request is approved, you will be granted the new virtual host.  If both virtual
hosts are direct subdomains of berkeley.edu, then you will be allowed to keep
your existing virtual host at its current URL until the end of the semester
following the rename, after which it will be reclaimed and eligible for
reassignment to another group or individual (e.g. if requested in the fall
semester, the old vhost will removed at the end of the following spring
semester). Note that for the purposes of this policy Winter break is considered
part of the Spring semester, and Summer break is considered part of the Fall
semester.

### Exceptions

Any exceptions to any policies outlined in this document must be approved by an
OCF General Manager, Site Manager, Deputy General Manager or Deputy Site
Manager in writing. Note that, due to university policy, we cannot grant any
exceptions allowing off-site hosting for any reason.
