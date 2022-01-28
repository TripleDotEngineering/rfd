---
title: "RFD-0001: Request for Discussion"
description: >
    RFD-0001 - A discussion about how we want to manage RFDs
date: 2022-01-28
authors: 
    - name: Josh Kaplan
      url: https://github.com/josh-kaplan
tags: ['rfd']
draft: true
status: draft
---

Requests for Discussion (RFDs) are intended to enable open discussions about
product enhancements, system design, and engineering practices.


<!--truncate-->

## Metadata

> What metadata do we need to keep track of?

- Authors
- Date
- State

## State

Triple Dot RFDs use the following states:

1. CREATED
2. DRAFT
3. DISCUSSION
4. ACCEPTED
5. IMPLEMENTED
6. ABANDONED

`CREATED` - This is the state once an RFD has been created. It may never enter 
this state in the index and should only be in this state when first created
by the author.

`DRAFT` - The RFD is being written by the author(s). It is not yet open for
discussion.

`DISCUSSION` - The RFD is open for discussion.

`ACCEPTED` - The discussion is not longer open and the RFD has been accepted.

`IMPLEMENETED` - Indicates that the RFD has been accepted and changes have been
incorporated into the relevant product(s). Not all RFDs will enter this state.
For example, this state won't be applicable to RFDs about best practices, 
procedures, or workflows.

`ABANDONED` - The RFD is no longer relevant and should be disregarded.


## Workflow

> What workflow will the RFD state change follow?

1. Allocate the RFD
    1. Create a branch called `allocate/<id>` where `<id>` is your RFD number.
    1. Write a brief description for the RFD.
    1. Update the state metadata to `draft` and open a PR.
    1. Open a pull request against the `main` branch. Once accepted, this will 
      allocate the RFD number and place the RFD in the `draft` state.
1. Open for discussion
    1. Created a branch of the format `draft/<id>`.
    1. Write the RFD
    1. Update the state to `discussion` and set draft to `false` and open a PR.
    1. This must be reviewed by at least 1 reviewer before approval.
    1. Once accepted, a new branch will be created `rfd/<id>` and a PR opened against `main`.
1. Have discussion
    1. State metadata should be set to `accepted` 
    1. Discussion should be had in the PR
1. Acceptance
    1. Once approved (process TBD), the PR will be merged and the discussion closed.


## Tooling

> What tooling do we need to support the above workflow?

1. `rfd make`
1. `rfd index`
1. `rfd validate` 

## See Also
 
- https://github.com/joyent/rfd
- https://oxide.computer/blog/rfd-1-requests-for-discussion
