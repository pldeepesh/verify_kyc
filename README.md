# verify_kyc
A django project with REST Api that reads PAN card images and extracts data.

A popular approach in the industry is to ask the person / entity to upload a scanned copy of their PAN card (in image or PDF format). It is then manually verified by a human agent that its:

● a valid PAN card

● authentic (i.e; not digitally morphed details)

● belongs to the same person.

The target of this application is to partially automate this process, and reduce human intervention.

At a high level, the application contains the following 2 components:

Extractor

The application exposes a REST API to extract structured information from a PAN card (image or PDF). Extracted information should contain at least the following fields:

    Permanent Account Number
    Name
    Date of Birth (if available)

Things to consider

● Choice of frameworks and other tools.
● Synchronous vs asynchronous processing.
● Scalability (How well can it handle lots of traffic?)
● Edge cases. (Note that the source file is sourced from the customer directly).
● Testability of the code with at least basic sanity tests.
● Code should be of production quality.

Human Feedback

Since user uploads can heavily vary in quality, our extractor may not always be accurate. This webapp will help collect feedback about accuracy from human agents. The feedback can be used to improve extractor in the future.

The human agent will be presented the original file, the structured information derived by the extractor. For each field, the agent will be able to take below actions:

    Do nothing (0 points).
    Mark as correct (1 Point).
    Mark as wrong (1 Point).
    Mark as wrong and provide correct value (2 Points).

This application will be used by multiple users (all staff of the company, for example). Since the goal of this application is to identify wrong parsing of extractor, the queue should be smartly ordered such that potential wrong ones should have priority over others.

The person earns corresponding points with each action taken. This web application displays a leadership board for all such users using this tool.

Things to consider

● Device-responsive and mobile-first (We’re living in mobile world, after all).
● Choice of frameworks and other tools.
● Graceful handling of errors and edge cases.
● Testability of the code with some basic sanity tests.
● Code should be of production quality.
