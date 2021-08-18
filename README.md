# Insecure Acebook



## What is Insecure Acebook?

This project has been adapted from the [Acebook Flask Template](https://github.com/makersacademy/acebook-flask-template). It has been modified to make it more insecure now! :raised_eyebrow: :unlock:

Some of the challenges may need you to experiment with the app running locally on your machine. Please refer to the repository linked above for instructions on how to set up the project.


## Getting started

Before we start making use of the SAST and DAST tools available within GitLab CI/CD, we encourage you to take a look at the application codebase.

The idea is for you to discuss in your teams and try to flag any potential security concerns that you may come up with.
What can you anticipate that could go wrong if we were to deploy this application to production?

Remember that the soonest we start taking security into consideration in the SLDC, the better. :closed_lock_with_key:

## Our GitLab Pipeline

How do we get started to implement security tools in our GitLab pipeline?

You will have to rename the `.example-gitlab-ci.yml` file in order for the pipeline to be triggered, as you have seen in previous weeks.

## Security Testing Tools

We are going to leverage the use of static and dynamic testing tools as part of our GitLab pipeline to help us identify potential vulnerabilities within our application.


### SAST

The `.gitlab-ci.yml` file is already set to work as is in order to run SAST jobs as part of the pipeline. Whenever you push the above file name change to your repository, a pipeline should trigger.

Downloading reports:

Once it's finished, you should be able to download the different reports generated. You can find these under `CI/CD` -> `Pipelines` -> `Artifacts` (the three dots on the right from the pipeline row that just run).

:interrobang: The different SAST-related reports should contain security concerns that have been found by the tool. Have a look at them and discuss in your teams:
- Are these security risks real vulnerabilities within our application?
- What could we do to mitigate the problem(s)?

The reports contain useful information linked to each found vulnerability that should help you find a solution (if needed).

If you found out that you should add some security implementations to your application to mitigate any of these, work on improving the application, push your code and analyse a new report generated from the tool.


### DAST

Once we are done with SAST, uncomment the three lines that are commented out at the moment in your `.gitlab-ci.yml` file.

After you commit these changes and push your code, an additional DAST stage should appear in our GitLab pipeline.

When this stage is done, you should be able to download the DAST report as JSON (following the same process as in the previous section).

:interrobang: This report should contain a list of vulnerabilities that have been found by the tool. Have a look at them and discuss in your teams:
- Are these security risks real vulnerabilities within our application?
- What could we do to mitigate the problem(s)?

The report contains useful information linked to each found vulnerability that should help you find a solution (if needed).

If you found out that you should add some security implementations to your application to mitigate any of these, work on improving the application, push your code and analyse a new report generated from the tool.


## Further comments on SAST and DAST tools

:see_no_evil: We should never blindly believe all of the vulnerabilities that are highlighted. In many occassions, these do not necessarily affect our projects or can be ignored safely. However, it is important that we understand what these mean to make a conscious decision.

Although these are great tools to help you assess how secure your application is before it gets deployed, **we should not only rely on them**.

It is also common to find out that these tools do not find all of the real issues within our applications, and here is when our security expertise will come in really handy to complement the job that these tools carry out for us.

### Did you notice that 1+ of the application templates are vulnerable to XSS attacks?

By default, Flask templates autoscape special characters (e.g. HTML tags). If we were to disable this feature for any reasons, we should be aware of XSS (Cross-Site Scripting) attacks.

If we do not have any sort of control of what the user may input into our application and we display such info without applying any security measures, the scenarios could be catastrophic.

<details>
  <summary markdown="span">:bulb: <b>Toggle this if you'd like some hints!</b></summary>

  Are we applying autoscape in any of the templates within our application? If so, in which one?
  Imagine the scenario where a user of our application chooses `<script>alert('You've been hacked!')</script>` as their post title. What would happen the next time we were to look at the posts feed?

  Executing such script would not be a disaster. However, a clever attacker could write a script that sends a request on our behalf (being logged in!) and perform any sort of malicious attack.

  As a rule of thumb, do not set `autoscape` to false if you don't need to. This way, we get standard HTML context filtering for variables in templates. Code and tags will be skipped and transformed to strings and won't be executed anymore.
</details>

## Bonus

As you have probably seen from running the SAST tools before, the application is vulnerable to Broken Authentication. This is not only due to the fact that the application config `secret key` is harcoded, but also due to the fact that the value for such key is in the Top 10 of easiest secrets to guess worlwide!

How could an attacker exploit such vulnerability in our system? :fire:

Depending on whether there's time/interest or not to find out more about this vulnerability (which can certainly be mitigated without necessarily having to reproduce it), your coach may organise a session to demonstrate how an attacker could go about bypassing the authentication system implemented in the application. :eyes:

### Resources
- [SAST in GitLab](https://docs.gitlab.com/ee/user/application_security/sast/)
- [DAST in GitLab](https://docs.gitlab.com/ee/user/application_security/dast/)
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Cross-Site Scripting (XSS)](https://flask.palletsprojects.com/en/2.0.x/security/#security-xss)
- [Broken Authentication](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)
- [Controlling Autoescaping in Flask App Templates](https://flask.palletsprojects.com/en/2.0.x/templating/#controlling-autoescaping)
- [Flask User Guide](https://flask.palletsprojects.com/en/2.0.x/)