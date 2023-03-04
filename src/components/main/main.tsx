import { Route, Routes } from "react-router-dom";
import { Calculator } from "../paths/pathWrapper";
import { Home } from "../wrapper";

export default function Main() {
    return(
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/calculator" element={<Calculator />} />
        </Routes>
    )
}