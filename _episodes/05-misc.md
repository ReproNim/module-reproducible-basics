---
title: "Other day-to-day reproducible practices"
teaching: 25
exercises: TODO
questions:
- How is *reproducibility* critical to fixing software bugs?
- What steps can you take toward sharing your studies reproducibly?
objectives:
- Underestand best practices for submitting bug reports
keypoints:
- If *you* can't reproduce it, it's likely that nobody else can.
- Having open sharing in mind from the beginning can simplify future reproducibility
---

---

In this final lesson, we'll cover some miscellaneous best practices
for reproducibility in basic day-to-day activities. Although individually
some practices may seem insignificant, they add up.

## A good bug report is a reproducible one

"Reproducibility" is at the heart of what constitutes a good bug report.


> ## References
>
> Additional materials:
>
> - [*How to Report Bugs Effectively* by Simon Tatham (1999) (10 min)](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html) --
>   a classic essay that remains apropos; provides an
>   overview of "good" and "bad" bug reports and how they can be expanded to provide sufficient information.
> - [Mozilla: Bug writing guidelines (15 min)](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines) --
>   although geared toward Mozilla products, this provides generally applicable
>   guidelines on how to structure bug reports
>
{: .callout}

Overall summary:

- If possible, **check if the issue persists with a newer version** of the
  software/dataset. If not, it was likely fixed and you'll need
  to upgrade. If the software comes from a centralized distribution,
  you can report the bug there, or request to have the package
  updated.

- **Do not try to describe the problem in your own words** if you are not
  100% sure what the problem is. And even if you are sure -- **provide
  a concise and reproducible example that demonstrates the problem**, be
  it a script or a list of steps for a GUI-driven package.

- **Make sure that your example is complete**; i.e. that it's not just a
  a code snippet without the necessary context (e.g., imports) to
  reproduce the issue.

  - Try to run it on another computer with a similar setup -- is it
    reproduce or not? Include that information in your report.

- **Provide relevant information**, such as:

  - the operating system and version

  - the version of the software in question and how it was installed
    (e.g., via a package manager, or manually from a source tarball,
    or from a Git repository)

  It's better to err on the side of being exhaustive.

- Right before you are ready to submit, **(re-)read your report
  yourself** to see if you can now get an idea of
  what might have gone wrong, or to see if you've
  provided all relevant information.

## Have reproducibility and openness in mind from the beginning

"*The devil is in the details*" and "*Talk is cheap, show me the code*"
(L. Torvalds, Linux project) are two common idioms pointing to the fact
that a verbal description alone, as typically condensed into a paper's
Methods section, is rarely sufficient to reproduce an empirical
result.

This is why it's so important to share relevant data, code, computation environments, etc.
However, if you delay preparing your materials for sharing, you might
find it difficult, if not impossible, to share your work later on --
as your project has progressed forward or may even be
completed. Keeping the goal of sharing in mind right from the
start will make sharing easier when you're actually
ready or asked to share.

> ## References
>
> Additional materials:
>
> - [Four aspects to make science open “by design” and not as an after-thought (15 min)](http://dx.doi.org/10.1186/s13742-015-0072-7) --
>   a brief communication on four considerations when starting
>   a project to facilitate sharing later on.
>
{: .callout}
