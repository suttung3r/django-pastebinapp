function langtype2mode(langtype) {
  console.log(langtype);
  switch (langtype) {
    case "PYTHON":
      return "text/python";
    case "RUST":
      return "text/rust";
    case "C":
    case "CPP":
    default:
      return "text/x-csrc";
  }
}
