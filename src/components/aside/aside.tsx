/**
 * @format
 */
import React from 'react';
import { NavLink } from 'react-router-dom';
import { LiComp, Lispan } from './components/li/liComp';
import {
	Paimon48,
	HomeSvg,
	CalcOutlineSvg,
	Hourglass,
	PfpSvg,
	GearSvg,
	LogoutSvg,
} from './icon/svgWrapper';

export default function Aside() {
	// TestVar
	const session = true;

	return (
		<aside className="mainAside">
			<div className="headerDiv">
				<div>
					<NavLink to="/" className="headerLink">
						<Paimon48 className="headerSvg" />
						<span className="headerText">Titulo Criativo</span>
					</NavLink>
				</div>
			</div>

			<div className="asideContent">
				<ul className="asideUl">
					<LiComp
						name="Home"
						to="/"
						Svg={<HomeSvg />}
						elemenClass={{
							navlink: 'liA_1',
							svgspan: 'liA_1_svgSpan',
							textspan: 'liA_1_text',
						}}
					/>

					<Lispan name="Tools" class="liSpan_text" />

					<LiComp
						name="Calculator"
						to="/calculator"
						Svg={<CalcOutlineSvg />}
						elemenClass={{
							navlink: 'liA_1',
							svgspan: 'liA_1_svgSpan',
							textspan: 'liA_1_text',
						}}
					/>

					<LiComp
						name="Artifacts"
						to="/artifacts"
						Svg={<Hourglass />}
						elemenClass={{
							navlink: 'liA_1',
							svgspan: 'liA_1_svgSpan',
							textspan: 'liA_1_text',
						}}
					/>

					<Lispan name="Options" class="liSpan_text" />

					<LiComp
						name="Profile"
						to="/profile"
						Svg={<PfpSvg />}
						elemenClass={{
							navlink: 'liA_1',
							svgspan: 'liA_1_svgSpan',
							textspan: 'liA_1_text',
						}}
					/>

					<LiComp
						name="Settings"
						to="/settings"
						Svg={<GearSvg />}
						elemenClass={{
							navlink: 'liA_1',
							svgspan: 'liA_1_svgSpan',
							textspan: 'liA_1_text',
						}}
					/>
					{session ? (
						<LiComp
							name="Logout"
							Svg={<LogoutSvg />}
							elemenClass={{
								navlink: 'liA_1',
								svgspan: 'liA_1_svgSpan logout',
								textspan: 'liA_1_text',
							}}
						/>
					) : (
						''
					)}
				</ul>
			</div>
		</aside>
	);
}
