$(document).ready(function () {
  // Client.setImageBasePath("/images");

  const container = document.getElementById("graph-container");
  InternalEvent.disableContextMenu(container);
  
  const graph = new CustomGraph(container);
  const propertyHandler = graph.getPlugin(
    PropertiesHandler.pluginId
  );
  window.graph = graph;
  
  // propertyHandler.labelOptions = undefined;
});
