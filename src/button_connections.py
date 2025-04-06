def setup_button_connections(ui, open_pdf_at_page, navigate_to_manual_page):
    """
    Conecta los botones a sus respectivas páginas en el QStackedWidget.
    """
    # Botones para la página Manual
    ui.ManualButton_1.clicked.connect(navigate_to_manual_page[0])
    ui.ManualButton_2.clicked.connect(navigate_to_manual_page[0])

    # Botones para otras páginas del QStackedWidget principal
    ui.FigthButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))  # Índice de la página de Combates
    ui.CharacterButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))  # Índice de la página de Personajes
    ui.RollButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(3))  # Índice de la página de Dados
    ui.MerchantButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(4))  # Índice de la página de Mercaderes
    ui.DiaryButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(5))  # Índice de la página de Diario
    ui.EstadisticButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(6))  # Índice de la página de Estadísticas

    ui.FigthButton_1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))  # Índice de la página de Combates
    ui.CharacterButton_1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))  # Índice de la página de Personajes
    ui.RollButton_1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(3))  # Índice de la página de Dados
    ui.MerchantButton_1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(4))  # Índice de la página de Mercaderes
    ui.DiaryButton_1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(5))  # Índice de la página de Diario
    ui.EstadisticButton_1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(6))  # Índice de la página de Estadísticas
    
    # Botones para desplegar los Libros
    ui.Manual_Libro1Buttom.clicked.connect(navigate_to_manual_page[1])
    ui.Manual_Libro2Buttom.clicked.connect(navigate_to_manual_page[2])
    ui.Manual_Libro3Buttom.clicked.connect(navigate_to_manual_page[3])
    ui.Manual_Libro4Buttom.clicked.connect(navigate_to_manual_page[4])
    ui.Manual_Libro5Buttom.clicked.connect(navigate_to_manual_page[5])
    ui.Manual_ApendiceButtom.clicked.connect(navigate_to_manual_page[6])

    # Botón para la página de Perfil
    ui.PerfilButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(7))  # Índice de la página de Perfil

    # Botón para la página de Configuración (Settings)
    ui.SettingButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(8))  # Índice de la página de Configuración

    # Botones para abrir secciones específicas del PDF
    ui.Manual_MetodoClasicoButton.clicked.connect(lambda: open_pdf_at_page(23))
    ui.Manual_MetodoLibreEleccionButton.clicked.connect(lambda: open_pdf_at_page(56))
    ui.Manual_SistemaDeJuegoButton.clicked.connect(lambda: open_pdf_at_page(72))
    ui.Manual_CaracteristicasButton.clicked.connect(lambda: open_pdf_at_page(76))
    ui.Manual_CompetenciasButton.clicked.connect(lambda: open_pdf_at_page(78))
    ui.ManualCaracteristicasSecundariasButton.clicked.connect(lambda: open_pdf_at_page(89))
    ui.Manual_MejoraPersonajeButton.clicked.connect(lambda: open_pdf_at_page(93))
    ui.Manual_PuntosVidaButton.clicked.connect(lambda: open_pdf_at_page(100))
    ui.Manual_PeligrosButton.clicked.connect(lambda: open_pdf_at_page(104))
    ui.Manual_CuracionButton.clicked.connect(lambda: open_pdf_at_page(112))
    ui.Manual_SecuenciaCombateButton.clicked.connect(lambda: open_pdf_at_page(116))
    ui.Manual_AccionesCombateButton.clicked.connect(lambda: open_pdf_at_page(118))
    ui.Manual_DanoButton.clicked.connect(lambda: open_pdf_at_page(126))
    ui.Manual_VariantesButton.clicked.connect(lambda: open_pdf_at_page(127))
    ui.Manual_ArmasButton.clicked.connect(lambda: open_pdf_at_page(130))
    ui.Manual_ArmadurasEscudosButton.clicked.connect(lambda: open_pdf_at_page(136))
    ui.Manual_RRIRRButton.clicked.connect(lambda: open_pdf_at_page(148))
    ui.Manual_ConsideracionesArsMagicaButton.clicked.connect(lambda: open_pdf_at_page(154))
    ui.Manual_HechizosButton.clicked.connect(lambda: open_pdf_at_page(155))
    ui.Manual_LanzamientoHechizosButton.clicked.connect(lambda: open_pdf_at_page(160))
    ui.Manual_GrimoriumButton.clicked.connect(lambda: open_pdf_at_page(163))
    ui.Manual_ComponentesMagicosButton.clicked.connect(lambda: open_pdf_at_page(235))
    ui.Manual_ComoConvertirseBrujaButton.clicked.connect(lambda: open_pdf_at_page(237))
    ui.Manual_ConsideracionesInicialesArsTeologicaButton.clicked.connect(lambda: open_pdf_at_page(243))
    ui.Manual_ElPoderDeLaFeButton.clicked.connect(lambda: open_pdf_at_page(246))
    ui.Manual_RitualesFideiButton.clicked.connect(lambda: open_pdf_at_page(250))
    ui.Manual_PecadosYPenitenciasButton.clicked.connect(lambda: open_pdf_at_page(266))
    ui.Manual_VotosYPromesasButton.clicked.connect(lambda: open_pdf_at_page(269))
    ui.Manual_RezandoALosSantosButton.clicked.connect(lambda: open_pdf_at_page(270))
    ui.Manual_TablaSantosButton.clicked.connect(lambda: open_pdf_at_page(271))
    ui.Manual_LaImagenDelDiabloButton.clicked.connect(lambda: open_pdf_at_page(277))
    ui.Manual_LosDemoniosSuperioresButton.clicked.connect(lambda: open_pdf_at_page(279))
    ui.Manual_DemoniosMenoresButton.clicked.connect(lambda: open_pdf_at_page(283))
    ui.Manual_EngendrosDelInfiernoButton.clicked.connect(lambda: open_pdf_at_page(293))
    ui.Manual_DemoniosElementales.clicked.connect(lambda: open_pdf_at_page(305))
    ui.Manual_NaturalezaAngelesButton.clicked.connect(lambda: open_pdf_at_page(310))
    ui.Manual_ArcangelesButton.clicked.connect(lambda: open_pdf_at_page(310))
    ui.Manual_JerarquiaCelestialButton.clicked.connect(lambda: open_pdf_at_page(313))
    ui.Manual_LaHuesteAngelicaButton.clicked.connect(lambda: open_pdf_at_page(315))
    ui.Manual_ServidoresMenoresButton.clicked.connect(lambda: open_pdf_at_page(318))
    ui.Manual_OrdenMalditoDescendenciaButton.clicked.connect(lambda: open_pdf_at_page(322))
    ui.Manual_AngelesTraidoresRebeldesButton.clicked.connect(lambda: open_pdf_at_page(324))
    ui.Manual_LosNumenButton.clicked.connect(lambda: open_pdf_at_page(329))
    ui.Manual_RazasYPueblosButton.clicked.connect(lambda: open_pdf_at_page(339))
    ui.Manual_AnimasyEspectrosButton.clicked.connect(lambda: open_pdf_at_page(346))
    ui.Manual_elPequeoPuebloButton.clicked.connect(lambda: open_pdf_at_page(356))
    ui.Manual_AnimalesFantasticosButton.clicked.connect(lambda: open_pdf_at_page(365))
    ui.Manual_OtrasCriaturasButton.clicked.connect(lambda: open_pdf_at_page(373))
    ui.Manual_AnimaliaButton.clicked.connect(lambda: open_pdf_at_page(382))
    ui.Manual_CoronaCastillaButton.clicked.connect(lambda: open_pdf_at_page(387))
    ui.Manual_CoronaAragonButton.clicked.connect(lambda: open_pdf_at_page(390))
    ui.Manual_ReinoGranadaButton.clicked.connect(lambda: open_pdf_at_page(391))
    ui.Manual_ReinoPortugalButton.clicked.connect(lambda: open_pdf_at_page(396))
    ui.Manual_CronologiaButton.clicked.connect(lambda: open_pdf_at_page(398))
    ui.Manual_JerarquiaSocialButton.clicked.connect(lambda: open_pdf_at_page(401))
    ui.Manual_UniversidadesButton.clicked.connect(lambda: open_pdf_at_page(408))
    ui.Manual_CiudadesVillasPueblosAldeasButton.clicked.connect(lambda: open_pdf_at_page(410))
    ui.Manual_LasMujeresDelMedievoButton.clicked.connect(lambda: open_pdf_at_page(426))
    ui.Manual_ComerciandoEnIntramurosButton.clicked.connect(lambda: open_pdf_at_page(413))
    ui.Manual_EstandoEnLaTabernaButton.clicked.connect(lambda: open_pdf_at_page(437))
    ui.Manual_DanzaMacabraButton.clicked.connect(lambda: open_pdf_at_page(443))
    ui.Manua_LaInquisicionMedievalButton.clicked.connect(lambda: open_pdf_at_page(445))
    ui.Manual_OrdenesMilitaresButton.clicked.connect(lambda: open_pdf_at_page(450))
    ui.Manual_LaFraternitaVeraLutisButton.clicked.connect(lambda: open_pdf_at_page(452))
    ui.Manual_LaCofradiaAnatermasButton.clicked.connect(lambda: open_pdf_at_page(453))
    ui.Manual_BeritHaMiniamButton.clicked.connect(lambda: open_pdf_at_page(454))
    ui.Manual_LaSectaDelMagisterueloButton.clicked.connect(lambda: open_pdf_at_page(456))
    ui.Manual_LosCaminantesButton.clicked.connect(lambda: open_pdf_at_page(457))
    ui.Manual_SobreDirectoresDeJuegoButton.clicked.connect(lambda: open_pdf_at_page(459))
    ui.Manual_LasReglasButton.clicked.connect(lambda: open_pdf_at_page(460))
    ui.Manual_ElMundoDeAquelarreButton.clicked.connect(lambda: open_pdf_at_page(462))
    ui.Manual_AventurasButton.clicked.connect(lambda: open_pdf_at_page(463))
    ui.Manual_AmbientacionButton.clicked.connect(lambda: open_pdf_at_page(465))
    ui.Manual_VisionesDeAquelarreButton.clicked.connect(lambda: open_pdf_at_page(467))
    ui.Manual_FabulaIButton.clicked.connect(lambda: open_pdf_at_page(476))
    ui.Manual_FabulaIButton_2.clicked.connect(lambda: open_pdf_at_page(494))
    ui.Manual_FabulaIButton_3.clicked.connect(lambda: open_pdf_at_page(498))
    ui.Manual_ApendiceIButton.clicked.connect(lambda: open_pdf_at_page(512))
    ui.Manual_ApendiceIIButton.clicked.connect(lambda: open_pdf_at_page(524))
    ui.Manual_ApendiceIIIButton.clicked.connect(lambda: open_pdf_at_page(526))
    ui.Manual_ApendiceIVButton.clicked.connect(lambda: open_pdf_at_page(528))
    ui.Manual_ApendiceVButoon.clicked.connect(lambda: open_pdf_at_page(530))
    ui.Manual_UltimasPalabrasButton.clicked.connect(lambda: open_pdf_at_page(533))
    ui.Manual_ChartaPersoaeButton.clicked.connect(lambda: open_pdf_at_page(534))
    ui.Manual_GlosarioButtom.clicked.connect(lambda: open_pdf_at_page(16))