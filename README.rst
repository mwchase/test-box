test-box
========
Utilities for a testing workflow in Python

I am unsure how generally useful this code is, but I've needed it twice, so I'm
making it a library.
To try to explain this briefly...

I developed a workflow for my hobby projects that is like unit testing, but is
not unit testing, I don't think.
The minimal goal is full code and branch coverage in testing, with the caveat
that executing code in a dependency does not count toward that dependency's
coverage.
For it to count, you have to actually have code in the tests for that component
that provides that coverage.
This lets me be lazy and not make mocks for my dependencies; that's why I don't
consider it unit testing.
It's **kind** of like integration testing? I think?

Anyway, it's a nice workflow, but it's got a problem: since each test module
gets its own run, the command-line diagnostics are all spread out.
Which is why there's logic to aggregate the test results, so you can actually
see what failed, and rerun it on its own.

None of this exists yet, because I have to generalize the logic, which is
excessively hardcoded to the project I first put this together for. In time...
