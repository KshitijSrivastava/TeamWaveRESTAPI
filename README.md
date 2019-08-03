# TeamWaveRESTAPI

A StackOverflow search app.
Requirement: (ref: https://api.stackexchange.com/docs/advanced-search)

1. Need for searching all available fields(parameter).
2. Should list the result with pagination.
3. Page/Data should be cached
4. Add Search limit per min(5) and per day(100) for each session


- /user -> Get and post of user data
- user/<int:pk> -> update and delete of user data
- question/ -> Get and post of question
- question/<int:pk> -> update and delete of questions
- answer/ -> get and post of answers
- answer/<int:pk> -> update and delete of answers
- search/advanced -> searching


- q - a free form text parameter, will match all question properties based on an
undocumented algorithm.

 - accepted - true to return only questions with accepted answers,
false to return only those without. Omit to elide constraint.

- answers - the minimum number of answers returned questions must have.

- body - text which must appear in returned questions' bodies.

- closed - true to return only closed questions, false to return only open ones.
 Omit to elide constraint.

- migrated - true to return only questions migrated away from a site,
false to return only those not. Omit to elide constraint.

- notice - true to return only questions with post notices, false to return
only those without. Omit to elide constraint.

- nottagged - a semicolon delimited list of tags, none of which will be present
on returned questions.

- title - text which must appear in returned questions' titles.

- user - the id of the user who must own the questions returned.

- url - a url which must be contained in a post, may include a wildcard.

- views - the minimum number of views returned questions must have.

- wiki - true to return only community wiki questions, false to return
 only non-community wiki ones. Omit to elide constraint.


 activity – last_activity_date
 creation – creation_date
 votes – score
 relevance – matches the relevance tab on the site itself
 activity is the default sort.
