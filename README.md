# RFD - Request for Discussion

A Request for Discussion (RFD) is an open format for capturing and refining
system designs, enhancements, and practices. 

See also: 
- https://github.com/joyent/rfd
- https://oxide.computer/blog/rfd-1-requests-for-discussion
-

---


## How to Create an RFD

### Allocate a new RFD number
RFDs are numbered starting at 1, and should be represented as zero-padded 4-digit 
numbers. Use the `rfd.py` tool, to allocate a new RFD number and generate some 
boiler-plate content from a template. To create a new RFD, run:

```bash
python tools/rfd.py make
```

This will prompt you for some basic information to fill out the initial metadata.
Note, that GitHub username is used to identify the author. This enables us to
more easily link the author URL to the person submitting the pull request.

**This workflow is subject to change per RFD-0001.**

Allocate the RFD

1. Create a branch called `allocate/<id>` where `<id>` is your RFD number.
1. Write a brief description for the RFD.
1. Update the state metadata to `draft` and open a PR.
1. Open a pull request against the `main` branch. Once accepted, this will 
  allocate the RFD number and place the RFD in the `draft` state.

Open for discussion

1. Created a branch of the format `open/<id>`.
1. Write the RFD
1. Update the state to `discussion` and set draft to `false` and open a PR.
1. This must be reviewed by at least 1 reviewer before approval.
1. Once accepted, a new branch will be created `rfd/<id>` and a PR opened against `main`.

Have discussion:
1. State metadata should be set to `accepted` 
1. Discussion should be had in the PR
1. Once approved (process TBD), the PR will be merged and the discussion closed.


### Write the RFD

TODO

### RFD Metadata

TODO


### RFD State

TODO