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

<div class="pub_filter_container">
  <button type="button" class="pub_filter_btn active" data-category="international_journal">
    <span class="filter_icon"><i class="fas fa-check-square"></i></span> International Journals
  </button>
  <button type="button" class="pub_filter_btn active" data-category="international_conference">
    <span class="filter_icon"><i class="fas fa-check-square"></i></span> International Conference Papers
  </button>
  <button type="button" class="pub_filter_btn active" data-category="domestic">
    <span class="filter_icon"><i class="fas fa-check-square"></i></span> Domestic Papers
  </button>
  <button type="button" class="pub_filter_btn active" data-category="patent">
    <span class="filter_icon"><i class="fas fa-check-square"></i></span> Patents
  </button>
</div>

<div class="pub_list">
{% assign current_year = 0 %}
{% for item in site.data.publications %}
  {% assign cat = "" %}
  {% if item.type == "international_journal" %}
    {% assign cat = "international_journal" %}
  {% elsif item.type == "international_conference" %}
    {% assign cat = "international_conference" %}
  {% elsif item.type == "domestic_conference" or item.type == "domestic_journal" %}
    {% assign cat = "domestic" %}
  {% elsif item.type == "patent" %}
    {% assign cat = "patent" %}
  {% endif %}

  {% if item.year != current_year %}
    {% assign current_year = item.year %}
    <h2 class="pub_year_header" data-year="{{ current_year }}">{{ current_year }}</h2>
  {% endif %}

  <div class="pub_item" data-category="{{ cat }}" data-year="{{ item.year }}">
    {% if item.type == "patent" %}
      <div class="pub_title">{{ item.title.ko }}</div>
      {% if item.title.en != nil and item.title.en != "" %}
      <div class="pub_subtitle">{{ item.title.en }}</div>
      {% endif %}
      <div class="pub_authors">
        {%- for inventor in item.inventors -%}
          {%- if forloop.last -%}{{ inventor }}{%- else -%}{{ inventor }}, {% endif %}
        {%- endfor -%}
      </div>
      <div class="pub_patent_status">
        {% if item.application != nil %}
        <span>출원: {{ item.application.number }} ({{ item.application.date }})</span>
        {%- endif -%}
        {%- if item.registration != nil -%}
        <span>, 등록: {{ item.registration.number }} ({{ item.registration.date }})</span>
        {% endif %}
      </div>
      <div class="pub_links">
        <span class="pub_button pub_button-patent">Patent</span>
        {% if item.doi != nil %}
        [
          <a href="{{ item.doi }}" target="_blank" rel="noopener noreferrer">DOI</a>
        ]
        {% endif %}
      </div>
    {% else %}
      <div class="pub_title">{{ item.title }}</div>
      <div class="pub_authors">
        {%- if item.type == "domestic_conference" or item.type == "domestic_journal" -%}
          {%- for author in item.authors -%}
            {%- if forloop.last -%}{{ author }}{%- else -%}{{ author }}, {% endif %}
          {%- endfor -%}
        {%- else -%}
          {%- assign author_count = item.authors.size -%}
          {%- if author_count == 1 -%}
            {{ item.authors[0] }}
          {%- elsif author_count == 2 -%}
            {{ item.authors[0] }} and {{ item.authors[1] }}
          {%- else -%}
            {%- for author in item.authors -%}
              {%- if forloop.last -%}and {{ author }}{%- else -%}{{ author }}, {% endif %}
            {%- endfor -%}
          {%- endif -%}
        {%- endif -%}
      </div>
      <div class="pub_venue">
        {% if item.venue.link != nil %}
        <a href="{{ item.venue.link }}" target="_blank" rel="noopener noreferrer">{{ item.venue.text }} {{ item.year }}</a>
        {% else %}
        <a>{{ item.venue.text }} {{ item.year }}</a>
        {% endif %}
      </div>
      <div class="pub_links">
        {% if item.type == "international_conference" %}
          <span class="pub_button pub_button-intconf">Int. Conf.</span>
        {% elsif item.type == "international_journal" %}
          <span class="pub_button pub_button-intjour">Int. Journal</span>
        {% elsif item.type == "domestic_conference" %}
          <span class="pub_button pub_button-domconf">Dom. Conf.</span>
        {% elsif item.type == "domestic_journal" %}
          <span class="pub_button pub_button-domjour">Dom. Journal</span>
        {% endif %}
        {% if item.links %}
        [
        {% for link in item.links %}
          {% if link[1] != nil and link[1] != "" %}
          <a href="{{ link[1] }}" target="_blank" rel="noopener noreferrer">{{ link[0] | capitalize }}</a>
          {%- unless forloop.last %} | {% endunless -%}
          {% endif %}
        {% endfor %}
        ]
        {% endif %}
        {% if item.award != nil %}
        <span class="pub_award">
          <i class="fas fa-award"></i> {{ item.award }}
        </span>
        {% endif %}
      </div>
    {% endif %}
    <div class="mt-4"></div>
  </div>
{% endfor %}

  <div id="no-pub-msg" class="no_pub_msg" style="display: none;">
    <p>No publications match the selected filters.</p>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var filterButtons = document.querySelectorAll('.pub_filter_btn');
  var pubItems = document.querySelectorAll('.pub_item');
  var yearHeaders = document.querySelectorAll('.pub_year_header');
  var noPubMsg = document.getElementById('no-pub-msg');

  function updateFilter() {
    var activeCategories = new Set();
    filterButtons.forEach(function(btn) {
      if (btn.classList.contains('active')) {
        activeCategories.add(btn.getAttribute('data-category'));
      }
    });

    var visibleCount = 0;
    var yearVisibleMap = {};

    pubItems.forEach(function(item) {
      var cat = item.getAttribute('data-category');
      var yr = item.getAttribute('data-year');
      if (activeCategories.has(cat)) {
        item.classList.remove('is-hidden');
        visibleCount++;
        yearVisibleMap[yr] = (yearVisibleMap[yr] || 0) + 1;
      } else {
        item.classList.add('is-hidden');
      }
    });

    yearHeaders.forEach(function(hdr) {
      var yr = hdr.getAttribute('data-year');
      if (yearVisibleMap[yr] && yearVisibleMap[yr] > 0) {
        hdr.classList.remove('is-hidden');
      } else {
        hdr.classList.add('is-hidden');
      }
    });

    if (noPubMsg) {
      noPubMsg.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  filterButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var icon = btn.querySelector('.filter_icon i');
      btn.classList.toggle('active');
      if (btn.classList.contains('active')) {
        if (icon) {
          icon.className = 'fas fa-check-square';
        }
      } else {
        if (icon) {
          icon.className = 'far fa-square';
        }
      }
      updateFilter();
    });
  });
});
</script>
