---
layout: article
titles:
  # @start locale config
  en      : &EN       Publications
  ko      : &KO       연구업적
  # @end locale config
key: publications
show_title: false
---

## International Papers

{% for item in site.data.publications %}
{% if item.type == "international_conference" or item.type == "international_journal" %}

<div class="pub_item">
  <div class="pub_title">{{item.title}}</div>
  <div class="pub_authors">
    {%- assign author_count = item.authors.size -%}
    {%- if author_count == 1 -%}
      {{ item.authors[0] }}
    {%- elsif author_count == 2 -%}
      {{ item.authors[0] }} and {{ item.authors[1] }}
    {%- else -%}
      {%- for author in item.authors -%}
        {%- if forloop.last -%} and {{author}} {%- else -%} {{author}}, {% endif %}
      {%- endfor -%}
    {%- endif -%}
  </div>
  <div class="pub_venue">
  {% if item.venue.link != nil %}
  <a href="{{item.venue.link}}">{{item.venue.text}} {{item.year}}</a>
  {% else %}
  <a>{{item.venue.text}} {{item.year}}</a>
  {% endif %}
  </div>
  <div class="pub_links">
  {% if item.type == "international_conference" %}
  <span class="pub_button pub_button-intconf">Conference</span>
  {% else %}
  <span class="pub_button pub_button-intjour">Journal</span>
  {% endif %}
  [ 
  {% for link in item.links %}
    <a href="{{ link[1] }}" target="_blank" rel="noopener noreferrer">{{ link[0] | capitalize }}</a>
    {%- unless forloop.last %} | {% endunless -%}
  {% endfor %}
  ]
  {% if item.award != nil %}
  <span class="pub_award">
  <i class="fas fa-award"></i> {{item.award}}
  </span>
  {% endif %}
  </div>
  <div class="mt-4"></div>
</div>
{% endif %}
{% endfor %}

## Domestic Papers

{% for item in site.data.publications %}
{% if item.type == "domestic_conference" or item.type == "domestic_journal" %}

<div class="pub_item">
  <div class="pub_title">{{item.title}}</div>
  <div class="pub_authors">
    {%- for author in item.authors -%}
      {%- if forloop.last -%} {{author}} {%- else -%} {{author}}, {% endif %}
    {%- endfor -%}
  </div>
  <div class="pub_venue">
  {% if item.venue.link != nil %}
  <a href="{{item.venue.link}}">{{item.venue.text}} {{item.year}}</a>
  {% else %}
  <a>{{item.venue.text}} {{item.year}}</a>
  {% endif %}
  </div>
  <div class="pub_links">
  {% if item.type == "domestic_conference" %}
  <span class="pub_button pub_button-intconf">Conference</span>
  {% else %}
  <span class="pub_button pub_button-intjour">Journal</span>
  {% endif %}
  [
  {% for link in item.links %}
    {%- if link[1] != nil and link[1] != "" -%}
    <a href="{{ link[1] }}" target="_blank" rel="noopener noreferrer">{{ link[0] | capitalize }}</a>
    {%- unless forloop.last %} | {% endunless -%}
    {%- endif -%}
  {% endfor %}
  ]
  {% if item.award != nil %}
  <span class="pub_award">
  <i class="fas fa-award"></i> {{item.award}}
  </span>
  {% endif %}
  </div>
  <div class="mt-4"></div>
</div>
{% endif %}
{% endfor %}


## Patents

{% for item in site.data.publications %}
{% if item.type == "patent"%}
<div class="pub_item">
  <div class="pub_title">{{item.title.ko}}</div>
  <div class="pub_subtitle">{{item.title.en}}</div>
  <div class="pub_authors">
    {%- for inventor in item.inventors -%}
      {%- if forloop.last -%} {{inventor}} {%- else -%} {{inventor}}, {% endif %}
    {%- endfor -%}
  </div>
  <div class="pub_patent_status">
  {% if item.application != nil %}
  <span>출원: {{item.application.number}} ({{item.application.date}})</span>
  {%- endif -%}
  {%- if item.registration != nil -%}
  <span>, 등록: {{item.registration.number}} ({{item.registration.date}})</span>
  {% endif %}
  </div>
  <div class="pub_links">
  <span class="pub_button pub_button-patent">Patent</span>
  {% if item.doi != nil %}
  [
    <a href="{{item.doi}}" target="_blank" rel="noopener noreferrer">DOI</a>
  ]
  {% endif %}
  </div>
  <div class="mt-4"></div>
</div>
{% endif %}
{% endfor %}
