---
layout: article
titles:
  # @start locale config
  en      : &EN       Members
  ko      : &KO       구성원
  # @end locale config
key: members
show_title: false
---

<style>
a.a-icon, a.a-icon:link, a.a-icon:visited {
  color: black;
}
.cell .card{
  margin-left:auto;
  margin-right:auto;
  max-width:200px;
}
.card__image{
  border-top-left-radius: 0.4rem;
  border-top-right-radius: 0.4rem;
  overflow:hidden;
}

.card__image>img{
  object-fit: cover;
  object-position: center;
  width:100%;
  height:200px;
}
</style>

{% for mt in site.data.membertypes %}
## {{mt.label}}
 
<div class="article-list grid grid--sm grid--p-3">
  {% for member in site.data.members %}
  {% if member.type == mt.type %}
  <div class="cell cell--6 cell--md-4 cell--lg-3">
    <div class="card">
      {% if mt.noimage != true %}
      <div class="card__image">
        {% if member.image != nil and member.image != "" %}   
        {% responsive_image_block %}
          path: assets/images/members/{{member.image}}
          class: 'member-photo'
        {% endresponsive_image_block %}   
        
        {% else %}
        {% responsive_image_block %}
          path: assets/images/members/unknown.jpg
          class: 'member-photo'
        {% endresponsive_image_block %}   
        {% endif %}
      </div>
      {% endif %}
      <div class="card__content">
        <div class="card__header2" style="line-height:1.2">
          <span><b>{{ member.name.en }}</b></span><br>
          <span>{{ member.name.ko }}</span><br>
        </div>
        {% if member.affiliation != nil %}
        <div style="line-height:1.2">
        {{member.affiliation}}
        </div>
        {% endif %}
        <div>
          {% if member.homepage != nil %}
          <a class="a-icon" href="{{member.homepage}}"><i class="fas fa-home"></i></a>
          {% endif %}
          {% if member.email != nil %}
          <a class="a-icon" href="mailto:{{member.email}}"><i class="fas fa-envelope"></i></a>
          {% endif %}
          {% if member.github != nil %}
          <a class="a-icon" href="{{member.github}}"><i class="fab fa-github"></i></a>
          {% endif %}
          {% if member.instagram != nil %}
          <a class="a-icon" href="{{member.instagram}}"><i class="fab fa-instagram"></i></a>
          {% endif %}
          {% if member.gscholar != nil %}
          <a class="a-icon" href="{{member.gscholar}}"><i class="fas fa-graduation-cap"></i></a>
          {% endif %}
          {% if member.youtube != nil %}
          <a class="a-icon" href="{{member.youtube}}"><i class="fab fa-youtube"></i></a>
          {% endif %}
        </div>
      </div>
    </div>
  </div>
  {% endif %}
  {% endfor %}
</div>


{% endfor %}
