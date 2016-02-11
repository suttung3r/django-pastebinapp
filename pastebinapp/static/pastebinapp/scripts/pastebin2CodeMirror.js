function langtype2mode(langtype) {
  console.log(langtype);
  switch (langtype) {
    case "PYTHON":
      return "text/x-python";
    case "RUST":
      return "text/x-rustsrc";
    case "C":
    case "CPP":
    default:
      return "text/x-csrc";
  }
}
