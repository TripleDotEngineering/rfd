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

Topics to discuss:

- metadata
- state
- workflow, branching strategy, approval

<!--truncate-->

## Metadata

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


## Workflow

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
