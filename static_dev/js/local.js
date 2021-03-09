var contentSections;
var contentVariants;
var contentIndex;

function loadSections() {
  return $.ajax({
    url: "/api/1.0/cs",
    type: "GET",
    cache: false,
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Accept", "application/json")
    }
  })
  .then(function(data) {
    contentSections = data;
  })
  .catch(function(err) {
    alert("Error loading content catalog.");
  });
}

function loadVariants() {
  return $.ajax({
    url: "/api/1.0/cv",
    type: "GET",
    cache: false,
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Accept", "application/json")
    }
  })
  .then(function(data) {
    contentVariants = data;
  })
  .catch(function(err) {
    alert("Error loading content catalog.");
  });
}

function buildContentIndex() {
  contentIndex = {
    byId: {},
    byName: {}
  };
  for (var i = 0; i < contentSections.length; ++i) {
    var cs = contentSections[i];
    cs.variants = [];
    contentIndex.byId[cs.id] = cs;
    contentIndex.byName[cs.name] = cs;
  }
  for (var i = 0; i < contentVariants.length; ++i) {
    var cv = contentVariants[i];
    contentIndex.byId[cv.section].variants.push(cv)
  }
}

loadSections().then(function() {
  loadVariants().then(function() {
    buildContentIndex();
    if (typeof(startApp) === "function") {
      startApp();
    }
  })
});
