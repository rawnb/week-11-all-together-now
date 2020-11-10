# Week 11 — All Together Now

## Lecture

* [Slide Deck](https://docs.google.com/presentation/d/1GbWm4IdKlq6KC1H4LFPdAUh_dHb8eA2QOXmkTyluAQc/edit?usp=sharing)

## Homework (not graded)

* Start the [Codecademy HTML course](https://www.codecademy.com/learn/learn-html)
  * Strongly recommend [Intro to HTML](https://www.codecademy.com/courses/learn-html/lessons/intro-to-html/exercises/intro)
  * Strongly recommend [Forms](https://www.codecademy.com/courses/learn-html/lessons/html-forms/exercises/forms-intro)
* Follow along and complete the Skeleton CSS Crash Course
  * Video: <https://www.youtube.com/watch?v=nVANwdryGVc>
  * Materials for the tutorial: <http://www.traversymedia.com/downloads/skeletoncrash.zip>
* Import some datasets into an AWS RDS PostgreSQL database
  * If you're looking for a dataset, try USGS' earthquake datasets: <https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv>. They provide information about the columns on [their site](https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php).


### Outline

0. Housekeeping
   * PostGIS day is coming: <https://info.crunchydata.com/blog/postgis-day-2020>
1. Final Project Checkins
   * Email me: groups and a time for us to meetup
2. PostgreSQL Revisited
   1. Getting data into PostgreSQL
   2. Updating data
     * Review update statements
     * If a geometry column does not exist, we need to create it: `ALTER TABLE tablename ADD COLUMN  geom(geometry, 4326);`
     * Don't forget to create an index: `CREATE INDEX tablename_geom_idx ON tablename USING GIST(geom);`
   3. Inserting data
     * If you have new data you want to append to an existing dataset, INSERT is the right tool for you
     * `UPSERT` If you want to insert data into the DB if it doesn't exist, but update otherwise, UPSERT is  the tool for you
   4. CREATE TABLE operations in PostgreSQL
     * Documentation: <https://www.postgresql.org/docs/12/sql-createtable.html>
     * Examples: <https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/>
     * There are a lot of ways to create tables in PostgreSQL
     * Usually you have to create an empty table first, then fill it with the data
     * Use Cases
       * Create a table from a query.
        * EASY! You don't have to create the table beforehand and know all the column names and types. Run  directly on the DB.
        * Useful if you want to create a table from a query you run all the time. E.g., create a table of  buffered points that you can then index.
           ```SQL
           CREATE TABLE new_table AS
           SELECT ST_Buffer(geom::geography, 100)::geometry as geom, ...
           FROM point_table;

           CREATE INDEX new_table_geom_idx ON new_table USING GIST(geom);
           ```
       * Create an empty table with specified schema (column names with types).
         ```SQL
           CREATE TABLE table_name (
              column1 datatype,
              column2 datatype,
              column3 datatype
           );
         ```
         Avoid errors
         ```SQL
         CREATE TABLE IF NOT EXISTS table_name (
            column1 datatype,
            column2 datatype,
            column3 datatype
         );
         ```
   5. Adding Columns
     * Reference: <https://www.postgresqltutorial.com/postgresql-add-column/>
     * Documentation: <https://www.postgresql.org/docs/12/sql-altertable.html>
3. Template Patterns with Flask
   1. Review full page template
   2. Templating in sub-pages
4. Sending results with forms / Live Demo
   0. Previously we had to manually construct API requests in the URL
   1. Structure of a form
   2. Form data is added to query strings in GET requests (request body for POSTs)

## CSS Frameworks

* [Skeleton](http://getskeleton.com) — Simple as far as CSS frameworks go but a little dated. More than sufficient for many things we will do in our class. Used in class demos, etc.
* [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/) — maybe the most popular CSS framework (and more), but more complicated for starting out
* [Bulma](https://bulma.io/) — fairly basic but powerful framework that lets you quickly build sites
* [WaterCss](https://watercss.netlify.app/)
* [Pure.css](https://purecss.io/)
* [Materialize](https://materializecss.com/)

### Icon libraries

* [Font Awesome](https://fontawesome.com/)
