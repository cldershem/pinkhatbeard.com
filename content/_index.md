+++
title = "contact"
template = "root.html"
+++
<table class="table is-striped">
  <tbody>

  {{ contact(label="email", info="cameron /at/ pinkhatbeard.com") }}
  {{ contact(label="email", info="cameron.dershem /at/ ocel.li") }}
  {{ contact(label="phone", info="+1.312.361.0322", link="tel:+013123610322") }}
  {{ contact(label="github", info="github.com/cldershem", link="http://github.com/cldershem") }}
  {{ contact(label="gitlab", info="gitlab.com/cldershem", link="http://gitlab.com/cldershem") }}
  {{ contact(label="gitlab phb", info="gitlab.com/pinkhatbeard", link="http://gitlab.com/pinkhatbeard") }}
  {{ contact(label="twitter", info="@jerknextdoor", link="https://twitter.com/jerknextdoor") }}
  {{ contact(label="resume", info="github.com/cldershem/resume", link="https://github.com/cldershem/Resume/blob/master/built/CameronDershemResume-Skills.pdf") }}
  {{ contact(label="freenode", info="jerknextdoor") }}
  {{ contact(label="irc.mozilla", info="pinkhatbeard") }}
  {{ contact(label="keybase.io", info="cldershem", link="https://keybase.io/cldershem") }}
  {{ contact(label="skype", info="cldershem", link="callto://cldershem") }}
  {{ contact(label="linkedin", info="Cameron Dershem", link="https://www.linkedin.com/in/cameron-dershem-1462389") }}
  {{ contact(label="google+", info="+CameronDershem", link="http://google.com/+CameronDershem") }}
  {{ contact(label="last.fm", info="cldershem", link="http://last.fm/user/cldershem") }}
  {{ contact(label="ttn", info="cldershem", link="https://www.thethingsnetwork.org/u/cldershem/") }}

  </tbody>
</table>
