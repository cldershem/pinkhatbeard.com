function get_random_adj() {
  var list_o_adjs = [
      "loud",
      "glasses",
      "talks a lot",
      "likes bikes",
      "long-haired",
      "hair farmer",
      "carries a purse",
      "wears a fannypack",
      ];
  var index = Math.floor(Math.random() * list_o_adjs.length);
  return list_o_adjs[index];
}

function get_random_tag() {
  var list_o_tags = ["t1", "t2"];
  var index = Math.floor(Math.random() * list_o_tags.length);
  return list_o_tags[index];
}

document.addEventListener('DOMContentLoaded', function () {
  var burger = document.getElementById("hamburger");
  var menu = document.getElementById("nav-menu");
  burger.addEventListener('click', function () {
    burger.classList.toggle('is-active');
    menu.classList.toggle('is-active');
  });
});
