---
title: "Version control systems"
teaching: 210
exercises: 40
questions:
- How and which version control systems help reproducibility?
objectives:
- Learn how to use version control systems to obtain, maintain, and
  share code and data
- Familiarize with an available variety of version control systems for
  code and data, and relevant tools based on them
- Review available 3rd party services and workflows which could be
  used to help to guarantee reproducibility of the results
keypoints:
- "Using VCS does not only improves sharing and collaboration, but
  also could be critical to assist and to guarantee reproducibility"
- "VCS could be used directly or serve a foundation for domain-specific tools"
---

> ## You can skip this lesson if you can answer these question? --->
>
>  - How to keep all your scripts, configuration, notes, and data
>    under version control systems, shareable with your collaborators,
>    and results automatically verified by continuous integration systems
{: .challenge}


## What is a “version control system" (VCS)?

Not surprisingly probably we all do version control of files,
documents and even data files, just do it in an ad-hoc version:

[![A Story Told in File Names by Jorge Cham, http://www.phdcomics.com/comics/archive_print.php?comicid=1323](../fig/borrowed/phd052810s.png)](http://www.phdcomics.com)

So, at large, VCS systems help to track versions of digital artifacts
such as code (scripts, source files), configuration files, images,
documents, data -- original or generated (as outcome of the analysis).
With proper annotation of changes, VCS becomes the lab notebook for
changing content in the digital world.  Since all versions are stored,
VCS makes it possible to provide any previous version at any later
point in time.  You can see how it could be important for reproducing
previous results -- if all necessary is contained within VCS, you just
need to get a previous version of your materials and carry out the
analysis using it.  You can also recover a file which you mistakenly
removed since previous version would be contained within VCS, so no
more "the cat ate my source code".  Even for those features it is
worthwhile placing any materials you care produce and care about under
some appropriate VCS.

Besides tracking changes, another main functions of VCS these days is
collaboration. VCSs are typically used not only locally but they allow
for transfer and aggregation of those versions (or changes) of your
work between collaborators.  By using some public services (such as
github.com) you can also make them available to other online services
which could for example be configured to react to any new change you
introduce and to perform prescribed actions.  Integration with such
services, which could be used for automated reanalysis of data and
verification that results still hold, provides another big benefit for
guaranteeing correct computations and reproducibility.

In this module we will first learn about

- general use of Git as the VCS to maintain not-so-large files (code,
configuration, etc)
- 3rd-party services worthwhile learning to integrate with your VCS on
public hosting portals (e.g. on github)
- VCS geared for managing data files
- additional VCS-based tools which could help you to get better
control of your digital research artifacts and notes.


## Git

> ## External teaching materials
>
> To gain a good general working knowledge of VCS and Git in
> particular, please go through following lesson and a tutorial:
>
> - [Software Carpentry: Version Control with Git (full: 2:30h, familiarize: 20m)](http://swcarpentry.github.io/git-novice/) --
>  a thorough lesson of the main git commands and workflows.  Please
> complete at least until `Licensing` submodule which will be a
> separate topic.
> - [Curious git: A curious tale (full: 30m, familiarize: 10m)](https://matthew-brett.github.io/curious-git/curious_journey.html)
>   -- useful read if you feel that "git internals" look like a black box to you.  This example guides you into
>   principles of Git without talking about Git.
> - (very optional, since this module is Git-based) [Software Carpentry: Version Control with Mercurial (full: 4h)](http://swcarpentry.github.io/hg-novice/)
{: .callout}


## 3rd party services

### Travis
### Circle-CI


## Git-annex


> ## External teaching materials
> -  [git-annex walkthrough](http://git-annex.branchable.com/walkthrough/) -
{: .callout}


## DataLad

> ## External teaching materials
> - [Examples of workflows](http://docs.datalad.org/en/latest/generated/examples/3rdparty_analysis_workflow.html)
{: .callout}

## Additional relevant helpers

- [sumatra](http://neuralensemble.org/sumatra) - manages
  and tracks projects based on numerical simulation or analysis,
  with the aim of supporting reproducible research. It can be thought
  of as an ''automated electronic lab notebook'' for
  simulation/analysis projects.

- [noworkflow](https://github.com/gems-uff/noworkflow) - captures a
  variety of provenance information and providing some analyses such
  as graph-based visualization, differencing over provenance trails,
  and inference queries.

- [etckeeper](http://etckeeper.branchable.com/) - a helper tool for
  anyone administering their Linux-based system, which would store and
  automatically commit any changes within `/etc` into a VCS of your
  choice.  With its help you could track changes in your system
  configuration which could be indispensable during system malfunction
  troubleshooting.


### Neuroimaging ad-hoc "versioning"

### Ad-hoc "version control"

- AFNI captures provenance information within output files which could
  be inspected using `3dinfo` command

