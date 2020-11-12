# Week 11 Lab — Building Websites

## Outline

* [HTML Overview](#html-overview)
* [Lab Exercises](#lab-practice)

## HTML Overview

1. High Level HTML
   * What is HTML?
     * "Markup" language that allows browsers to interpret how a website should look.
    * "While HTML is used to define the structure and semantics of your content, CSS is used to style it and lay it out. For example, you can use CSS to alter the font, color, size, and spacing of your content, split it into multiple columns, or add  animations and other decorative features."
     * Consists of tags: `<a href='https://...'>Look at this link!</a>`
      ![](https://media.prod.mdn.mozit.cloud/attachments/2014/04/09/7659/a731e40efad1f6e0b728bfcf86c0035b/anatomy-of-an-html-element.png)
     * Tags have attributes
      ![](https://media.prod.mdn.mozit.cloud/attachments/2014/11/14/9345/99516bbeb470af58b608d17bb30e53e6/grumpy-cat-attribute-small.png)
       * The hyperlink tag [`a`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) has the following attributes:
         * `href`: Website or part of page to link to
         * `target`: How to open the new page (new tab, same tab, etc.)
         * `title`: Additional information about the page being linked to
         * `style`: How to style the text displayed for the link. Note: this is available for most HTML tags.
     * Tags are styled by a language called CSS (Cascading Style Sheets)
   * Basic Structure of a Website
     * Full basic HTML
       ```HTML
       <!DOCTYPE html>
       <html>
         <head>
           <meta charset="utf-8">
           <title>My test page</title>
         </head>
         <body>
           <p>This is my page</p>
         </body>
       </html>
       ```
2. HTML in more depth
   * Contents of `head`
     * [`title`](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML#Adding_a_title)
     * [favicon](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML#Adding_custom_icons_to_your_site)
     * [CSS & JavaScript links](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML#Applying_CSS_and_JavaScript_to_HTML)
     * Stylesheet definitions
     * [meta tags](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML#Metadata_the_%3Cmeta%3E_element)
   * Contents of [`body`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body) — the content of your website, consisting of text, HTML tags,  media (images, video, etc.).
     * Important tags
       * [`p`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) — paragraph (block) — for writing larger blocks of text
         ```HTML
         <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras metus.</p>
         ```
       * [`a`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) — hyperlink (inline) — Used for making links to pages
         ```HTML
         Check out <a href="https://github.com/MUSA-509/">MUSA 509's class page</a>
         ```
       * [`b`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b), [`i`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i) — bold and italic (inline) — for emphasis of parts of text
         ```HTML
         This is <b>MUSA 509</b>.
         ```
       * [`h1`, `h2`, `h3`, etc.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) — heading elements (block) — `h1` is the largest, and they get progressively smaller as the number gets larger up to 6.
       * [`img`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) — for embedding images in webpages
         ```HTML
         <img src="https://i.pinimg.com/originals/a7/c6/9c/a7c69cb3cf2e5a0d1fb9f7211b7bea2a.gif" title="Sleepy cat in a bowl" />
         ```
       * [`ul`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), [`ol`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol), [`li`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) — unordered list (`ul`) and ordered list (`ol`) (both block). These, along with each list item `li` make lists.
         ```HTML
         <ul>
           <li>This is the first item</li>
           <li>This is the second item</li>
         </ul>
         ```
       * [`table`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table) — makes tables (block). Use with [`tr`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) and [`td`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) to define rows and columns. Define header rows with [`th`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th).
         ```HTML
         <table>
           <tr><th>cookie type</th><th>quantity</th></tr>
           <tr><td>pecan</td><td>10</td></tr>
           <tr><td>chocolate chip</td><td>15</td></tr>
         </table>
         ```
        * [`div`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) — a container for page elements (block). Really useful for combining multiple tags and applying positioning styles
        * [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span) — a container for inline page elements (inline).
     * [Block](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) versus [Inline](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements)
       ```HTML
       <div class="container">
         Lots of HTML
       </div>
       ```
3. CSS — CSS is a language for defining the styles of HTML pages, which includes colors, fonts, positioning, and more. Check out [Mozilla's CSS course](https://developer.mozilla.org/en-US/docs/Learn/CSS) for more details.
   * [Styles available](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference)
   * A grouping of styles in a style sheet is called a class. You define a class like so:
     ```CSS
     .penn_themed {
       color: #990000;
       border: 2px solid #011F5b;
       background-color: #eee;
     }
     ```
   * Styles can be defined in a few ways:
     * Within HTML tags, along with styles defined in a class
       ```HTML
       <p style="padding: 5px; border-radius: 15px; width: 25%;" class="penn_themed">This is a Penn-themed paragraph block.</p>
       ```
     * As a CSS section within an HTML document
       ```HTML
       <head>
         <style>
           p {
             background-color: #8ABB55;
           }
           .highlight {
             background-color: #ee3;
           }
         </style>
       </head>
       ```
     * As external (or local) files. Here we are linking to the Skeleton CSS framework
       ```HTML
       <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css">
       </head>
       ```
       Note: in Flask, we link to local stylesheets by using the path constructed from `url_for('static', filename='path/to/stylesheet.css')`. See [this StackOverflow post](https://stackoverflow.com/a/16353060/3159387) for more information. See also [Flask docs on static files](https://flask.palletsprojects.com/en/1.1.x/tutorial/static/).

## Lab Practice

For all of the exercises here, let's use our browser's developer tools to inspect the pages.

**Accessing Developer Tools**
> Right-click an element on the page and select Inspect to jump into the Elements panel. Or press Command+Option+C (Mac) or Control+Shift+C (Windows, Linux, Chrome OS).

### Exercises


0. Open the [`html_elements.html`](html_elements.html) both in your browser and in your text editor.
1. Using the [`html_elements.html`](html_elements.html) HTML file:
   1. Fill in the `title` tags in the `head`
   2. Page Title
      * Add an `h1` saying something like `MUSA 509 Week 11 Lab Problem 1`
      * Add a `p` beneath this describing the lab this week
   3. Hyperlink Section
      * Add an `h2` with a title of 'Hyperlinks'
      * Create some text with a hyperlink to our class repo: `https://github.com/MUSA-509/week-11-all-together-now`
   4. Image Section
      * Add an `h2` with at title of 'Images'
      * Include an image (e.g., a cat gif)
   5. List Section
      * Add an `h2` with a title of 'Lists'
      * Create a list (e.g., ToDo list, list of cookies you like, etc.)
2. Using the `html_elements.html` HTML file, add the Skeleton CSS link to the appropriate section of the HTML page:
   ```HTML
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css">
   ```
   What happens after the stylesheet is loaded?
3. Building a site — Let's tinker with the app that's in this week's repo
   1. Get going
      * Start up the conda environment: `conda activate musa509week6`
      * Make sure you have the [`pg-credentials.json`](https://canvas.upenn.edu/courses/1533813/files/89654914/download?download_frd=1) file in the directory.
      * Start the app: `python app.py`
   2. Walk through the app
   3. Reference [Skeleton CSS Documentation](http://getskeleton.com/)
   4. Change button colors
   5. Add new button to add new functionality — random neighborhood selector
