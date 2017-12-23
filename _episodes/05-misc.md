---
title: "Other day-to-day reproducible practices"
teaching: 25
exercises: TODO
questions:
- How does *reproducibility* help in fixing bugs?
- What can you do to be ready to share your studies reproducibly?
objectives:
- Explain best practices on submitting bug reports
keypoints:
- If *you* cannot reproduce it -- it is unlikely that anyone else can
- Having open sharing in mind from the beginning can simplify future reproducibility
---

---

In this lesson, let’s cover some other relatively small
aspects of reproducibility in basic day-to-day activities.

## A good bug report is a reproducible one

“Reproducibility” is at the heart of what constitutes a good bug report.


> ## References
>
> Additional materials:
>
> - [How to Report Bugs Effectively  *by Simon Tatham* (1999) (10 min)](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html)
>   A classical essay, which remains apropos.  It provides an
>   overview of various aspects on what "bad" and "good" reports are and how they could be expanded to provide sufficient information
> - [Mozilla: Bug writing guidelines (15 min)](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines)
>   Although it concentrates solely on Mozilla products, it provides good and
>   generally applicable guidelines on how to phrase and structure
>   bug reports
>
{: .callout}

Overall summary:

- If possible, **check if the issue persists with a newer version** of the
  software/dataset. If not -- it was likely fixed and you will need
  to upgrade. Or, if the software comes from a centralized distribution,
  you might like to report it there or ask to have the package
  updated there.

- **Do not try to describe the problem in your own words** if you are not
  100% sure what the problem is. And even if you are sure -- **provide
  a concise and reproducible example that demonstrates the problem**, be
  it a script, or a list of steps in a GUI-driven software.

- **Make sure that your example is complete**, i.e. that is not just a
  ripped out piece without necessary imports etc. and that it does
  reproduce the issue
  
  - Try to run it on another computer with a similar setup -- does it
    reproduce or not? Include that information in your report.

- **Provide relevant information**, such as:

  - The operating system and its version

  - The version of the software in question and how it was installed
    (e.g. via a package manager, or manually from a source tarball
    or from a Git repository)

- Right before you are ready to submit -- **(re-)read your report
  yourself** and see if you can now get an idea of
  what could have gone wrong, or to see if you feel like you have
  provided all possibly relevant information

## Have reproducibility and openness in mind from the beginning

"*The devil is in the detail*” and "*Talk is cheap, show me the code*"
(L. Torvalds, Linux project) are two common idioms pointing to the fact
that a verbal description alone, as typically condensed into a paper's
Methods section, is rarely sufficient to reproduce an empirical
result.  

That is why it is important to share also relevant data, code, description
of the computation environments, etc. 
However, if you delay preparing your materials so they are ready to be shared, you might
find it difficult, if not impossible, to actually be able to
share your work later on as your project has progressed forward or may even be 
completed. Having the possibility of sharing in mind right from the
beginning will make actual sharing a much easier task when you are actually 
ready or are asked to share.

> ## References
>
> Additional materials:
>
> - [Four aspects to make science open “by design” and not as an after-thought (15 min)](http://dx.doi.org/10.1186/s13742-015-0072-7)
>   A brief communication on four aspects to be taken care of at the
>   beginning of your project to make it easy to share later on.
>
{: .callout}
