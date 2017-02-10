---
title: "Other day-to-day reproducible practices"
teaching: 25
exercises: TODO
questions:
- How does *reproducibility* help in fixing bugs?
- What can you do to be ready to share your studies and have them be reproducible?
objectives:
- Explain best practices on submitting bug reports
keypoints:
- If you cannot reproduce *it* -- it is unlikely that anyone else can
- Having open sharing in mind from the beginning could simplify future reproducibility
---

---

In this lesson we would like to cover some other relatively small
aspects of *reproducibility* in basic day-to-day activities.

## A good bug report is a reproducible one

Although it might come as a surprise, “reproducibility” is in the
heart of what constitutes a good bug report.


> ## References
>
> Additional materials:
>
> - [How to Report Bugs Effectively  *by Simon Tatham* (1999) (10 min)](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html)
>   A classical essay, which remains apropos.  It provides an
>   overview of various aspects on what "bad" and "good" reports and how they could be expanded to
>   provide sufficient information
> - [Mozilla: Bug writing guidelines (15 min)](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines)
>   Although concentrating on Mozilla products, it provides good
>   generally applicable guidelines how to phrase and structure
>   bug reports
>
{: .callout}

Overall summary:
- If possible, **check if issue persists with a newer version** of the
  software/dataset. If not -- it was likely fixed and you would need
  to upgrade, or if software comes from a centralized distribution,
  you might like to report it there or ask to have package being
  updated there
- Do not try to describe the problem in your own words if you are not
  100% sure what the problem is. An even if you are sure -- **provide
  concise and reproducible example that demonstrates the problem** be
  it a script, or a list of steps in a GUI-driven software
- **Make sure that your example is complete**, i.e. that is not just a
  ripped out piece without necessary imports etc. and that it does
  reproduce the issue
  - Try to run it on another computer with similar setup -- does it
    reproduce or not, include that information in your report
- Do not forget to **provide relevant information**, such as:
  - The operating system and its version
  - The version of the software in question and how it was installed
    (e.g. via a package manager, or manually from a source tarball
    or a git repository)
- Right before you are ready to submit -- **(re-)read your report
  yourself** and see if you possibly could now get an idea of
  what could have gone wrong, or to see if you feel like you have
  provided all possibly relevant information

## Have reproducibility and openness in mind from the beginning

"*The devil is in the detail*" and "*Talk is cheap, show me the code*"
(L.Torvalds, Linux project) are two common idioms pointing to the fact
that a verbal description (as e.g. typically condensed into a paper's
Methods section) alone is rarely sufficient to reproduce an empirical
result.  That is why it is important to prepare to have not only the
summary paper to be shared, but also relevant data, code, description
of the computation environments, etc.  However, if you wait to prepare
to share later, as your project has progressed or may be even complete, you might
make it difficult if not impossible to actually be able to
share your work.  Having sharing of your materials in mind right from the
beginning should make actual sharing when you are ready to share a
much easier task.

> ## References
>
> Additional materials:
>
> - [Four aspects to make science open “by design” and not as an after-thought (15 min)](http://dx.doi.org/10.1186/s13742-015-0072-7)
>   A brief communication on four aspects to be taken care off at the
>   beginning of your project to make it easy to share later on.
>
{: .callout}
